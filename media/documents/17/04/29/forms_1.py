from django.contrib.auth.forms import AuthenticationForm
from django import forms

from polls.models import Document, LibraryModel


class Loginform(AuthenticationForm):
    username = forms.CharField(label="username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class DocumentForm(forms.Form):
    class Meta:
        model = Document
        fields = ('description', 'document',)


class Libraryform(forms.Form):
    category = forms.CharField(label="category", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'category'}))
    name = forms.CharField(label="name", max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name'}))
    creator = forms.CharField(label="creator", max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'creator'}))
    screenshots1 = forms.ImageField(label="screenshot1",
                                    widget=forms.FileInput(attrs={'class': 'form-control'}))
    screenshots2 = forms.ImageField(label="screenshot2",
                                    widget=forms.FileInput(attrs={'class': 'form-control'}))
    screenshots3 = forms.ImageField(label="screenshot3", widget=forms.FileInput(attrs={'class': 'form-control'}))
    githublink = forms.CharField(label="githublink", max_length=256,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'githublink'}))
    websitelink = forms.CharField(label="websitelink", max_length=256,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'websitelink'}))
