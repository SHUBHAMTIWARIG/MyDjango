from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': "username"}))
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
