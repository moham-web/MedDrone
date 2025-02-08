from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")