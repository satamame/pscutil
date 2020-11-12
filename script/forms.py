from django import forms


class PredictForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(
            attrs={'accept': 'text/*'}
        )
    )
