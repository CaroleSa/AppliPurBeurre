#! /usr/bin/env python3
# coding: UTF-8

""" Views """


# Imports
from django.shortcuts import render
from account.forms import Account
from account.models import User
import hashlib




def account(request):
    form = Account()
    context = {'form': form}

    # get the e-mail entered by the user
    email = form.cleaned_data['e_mail']
    # searched e-mail in the database
    email = User.objects.get(e_mail=email)

    if email.exists() is True:
        # get and encrypted the password entered by the user
        password = form.cleaned_data['password'].encode()
        encrypted_password = hashlib.sha1(password).hexdigest()

        # get encrypted password in the database
        data = User.objects.filter(email=email)
        password_database = data.objects.values_list('password')

        if encrypted_password == password_database:
            context["user"] = "True"

        else:
            context["user"] = "False"
            context["error"] = "Le mot de passe n'est pas correct."

    else:
        context["error"] = "Cette adresse e-mail n'existe pas."

    return render(request, 'account/account.html', context)
# indiquer pourquoi l'adresse mail pas bonne ou mot de passe

def create_account(request):
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        form = Account(request.POST)

        if form.is_valid() is True:

            # get user's e-mail
            email = request.POST.get('e_mail')

            # get and encrypted user's password
            password = request.POST.get('password').encode()
            encrypted_password = hashlib.sha1(password).hexdigest()

            # insert user's data in the database
            User.objects.create(e_mail=email, password=encrypted_password)

            context["message"] = "Votre compte a bien été créé."

        else:
            email = request.POST.get('e_mail')
            email_database = str(User.objects.get(e_mail__icontains=email))

            if email == email_database:
                context["message"] = "Ce compte existe déjà."

            else:
                # verif .com .fr nombre de chiffre mot de pass, majuscules dans email
                # Form data doesn't match the expected format.
                # Add errors to the template.
                context["message"] = "Message d'erreur"

    return render(request, 'account/create_account.html', context)


def my_account(request):
    context = {}

    return render(request, 'account/my_account.html', context)
