#! /usr/bin/env python3
# coding: UTF-8

""" Forms """


# Import
from django.forms import ModelForm, TextInput, EmailInput
from account.models import User



class CreateAccount(ModelForm):
    class Meta:
        model = User
        fields = ["e_mail", "password"]
        widgets = {
            'e_mail': EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Adresse E-mail'}),
            'password': TextInput(attrs={'class': 'form-control', 'Placeholder': 'Mot de passe', 'type': 'password', 'maxlength': '8', 'minlength':"8"})
        }


class AccessAccount(ModelForm):
    class Meta:
        model = User
        fields = ["e_mail", "password"]
        widgets = {
            'e_mail': EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Adresse E-mail'}),
            'password': TextInput(attrs={'class': 'form-control', 'Placeholder': 'Mot de passe', 'type': 'password', 'maxlength': '8', 'minlength':"8"})
        }