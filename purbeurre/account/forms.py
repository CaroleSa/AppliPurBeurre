#! /usr/bin/env python3
# coding: UTF-8

""" Forms """


# Import
from django.forms import ModelForm, TextInput, EmailInput
from account.models import UserAccount



class Account(ModelForm):
    class Meta:
        model = UserAccount
        fields = ["e_mail", "password"]
        widgets = {
            'e_mail': EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Adresse E-mail'}),
            'password': TextInput(attrs={'class': 'form-control', 'Placeholder': 'Mot de passe à 8 caractères', 'type': 'password', 'maxlength': '8', 'minlength':"8"})
        }
