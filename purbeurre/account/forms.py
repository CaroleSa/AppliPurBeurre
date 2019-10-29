#! /usr/bin/env python3
# coding: UTF-8

""" Forms """


# Import
from django.forms import ModelForm, TextInput, EmailInput
from account.models import User



class Account(ModelForm):
    class Meta:
        model = User
        fields = ["e_mail", "password"]
        widgets = {
            'password': TextInput(attrs={'class': 'form-control', 'Placeholder': 'Mot de passe', 'type': 'password'}),
            'e_mail': EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Adresse E-mail'})
        }
