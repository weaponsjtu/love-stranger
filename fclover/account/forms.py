from django import forms

class SigninForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
