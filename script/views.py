import pickle

from django.views.generic import TemplateView, FormView, DetailView
from django.urls import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from psc_parse import JumanPsc, PscClass
from psc_parse.model import predict

from .models import Script
from .forms import PredictForm


class ScriptTop(TemplateView):
    '''トップメニューの画面
    '''
    template_name = 'script/top.html'


class ScriptPredict(FormView):
    '''書式不明の台本を読み込む画面
    '''
    template_name = 'script/predict.html'
    form_class = PredictForm

    def post(self, request, *args, **kwargs):
        # アップロードされたファイルの内容を文字列として取得する
        with request.FILES['file'].open(mode='r') as f:
            sc_text = f.read().decode()

        # 行の種類を予測する
        line_types = self.predict_line_types(sc_text)

        # 台本テキストと行の種類を保存する
        script = Script(
            plain_text=sc_text,
            line_types=line_types
        )
        script.save()

        # ラベル付け画面へリダイレクトする
        token = script.token
        url = reverse_lazy('script:label', kwargs={'slug': token})
        response = HttpResponseRedirect(url)

        return response

    def predict_line_types(self, sc_text):
        '''台本テキストから行の種類を予測して改行で繋げて返す
        '''
        # 形態素解析器
        juman = JumanPsc(command=settings.JUMAN_COMMAND,
            option=settings.JUMAN_OPTION)

        # 予測モデル
        with open(settings.PSC_PARSE_MODEL_PATH, 'rb') as f:
            tree = pickle.load(f)

        # 台本を行に分けて、各行の種類を予測する
        lines = sc_text.splitlines()
        classes = predict(juman, tree, lines)

        # 行の種類を改行文字で繋げて返す
        line_types = (str(c) for c in classes)
        return '\n'.join(line_types)


class ScriptLabel(DetailView):
    '''読み込んだ台本のラベル (行の種類) を修正する画面
    '''
    template_name = 'script/label.html'
    model = Script
    slug_field = 'token'

    type_strings = [
        "題名",
        "著者名",
        "登場人物見出し",
        "登場人物",
        "柱1",
        "柱2",
        "柱3",
        "ト書き",
        "セリフ",
        "エンドマーク",
        "コメント",
        "空行",
        "登場人物(続き)",
        "ト書き(続き)",
        "セリフ(続き)",
        "コメント(続き)",
    ]

    def get_context_data(self, **kwargs):
        '''テンプレートに渡すパラメタを改変する
        '''
        context = super().get_context_data(**kwargs)

        # テキストを行ごとに分けてリストにする
        sc_lines = self.get_object().plain_text.splitlines()

        # 行の種類を行ごとに分けてリストにし、可読な文字列のリストも作る
        line_types = self.get_object().line_types.splitlines()
        line_type_strs = [self.type_strings[int(t)] for t in line_types]

        context['lines'] = zip(line_types, line_type_strs, sc_lines)
        context['type_strings'] = self.type_strings
        return context

    def post(self, request, *args, **kwargs):
        return super().post()
