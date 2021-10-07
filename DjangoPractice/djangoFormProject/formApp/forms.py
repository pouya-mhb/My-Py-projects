from django import forms

class MHBForm (forms.Form):
    number1 = forms.DecimalField()
    number2 = forms.DecimalField()
