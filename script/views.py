from django.views.generic import TemplateView


class ScriptTop(TemplateView):
    '''トップのメニュー画面
    '''
    template_name = 'script/top.html'
