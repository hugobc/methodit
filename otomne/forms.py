from django import forms
class InputForm(forms.Form):
    your_name = forms.CharField(label='',
widget=forms.TextInput(attrs={#'placeholder': 'How may I assist You ?',
                                  #'autofocus': 'autofocus',
                                  'autocomplete': 'on', # may be set off
                                  'size': '55',
                                  'style': 'font-size: 30px',
                           }))
