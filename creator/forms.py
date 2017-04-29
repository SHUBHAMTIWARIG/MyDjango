from django import forms
from django.contrib.auth.forms import AuthenticationForm


class creator_form(forms.Form):
    name = forms.CharField(label="Creator Name", max_length=30,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'name': "username"}))

    email = forms.EmailField(label="Email Address", widget=forms.TextInput(attrs={'class': 'form', 'name': 'email'}))
    password = forms.CharField(label="password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    contact = forms.IntegerField(label="Contact No",widget=forms.TextInput(attrs={'class': 'form-control', 'name': "contact"}))
    option = (('py', 'PYTHON DJANGO'), ('J', 'core java'), ('AJ', 'Advance java'), ('Asp', 'visual stdio'), ('cpp', 'oops'))
    area_of_intrest = forms.MultipleChoiceField(label="Area_Of_Intrest", widget=forms.CheckboxSelectMultiple, choices=option)
    age = forms.IntegerField(label="Age",widget=forms.TextInput(attrs={'class': 'form-control', 'name': "age"}))
    profile_image = forms.ImageField(label="upload your image")
