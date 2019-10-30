#! /usr/bin/env python3
# coding: UTF-8

""" Views """


# Imports
from django.shortcuts import render
import re
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

        # if the data entered by the user is valid
        if form.is_valid() is True:
            # get user's data
            email = request.POST.get('e_mail')
            password_control = request.POST.get('passwordControl')
            password = request.POST.get('password')

            # if e-mail is valid
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is not None:

                # if password and password control are the same
                if password_control == password:
                    # encrypted user's password
                    password = password.encode()
                    encrypted_password = hashlib.sha1(password).hexdigest()
                    # insert user's data in the database
                    User.objects.create(e_mail=email, password=encrypted_password)
                    # create confirmation message
                    context["message"] = "Votre compte a bien été créé."
                    context["color"] = "green"

                # if password and password control aren't the same
                else:
                    # create error message
                    context["message"] = "Vos mots de passe ne sont pas identiques."
                    context["color"] = "red"

            # if e-mail isn't valid
            else:
                context["message"] = "Cet e-mail n'est pas valide."
                context["color"] = "red"

        # if the data entered by the user is not valid
        else:
            # if e-mail is not valid
            email = request.POST.get('e_mail')
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is None:
                # create error message
                context["message"] = "Cet e-mail n'est pas valide."
                context["color"] = "red"

            # if e-mail is valid
            else:
                email_database = str(User.objects.get(e_mail__icontains=email))

                # if user's e-mail exists to the database
                if email == email_database:
                    # create error message
                    context["message"] = "Ce compte existe déjà."
                    context["color"] = "red"

                # if user's e-mail don't exists to the database
                else:
                    password = request.POST.get('password')
                    # if user's password is too long
                    if len(password) > 8:
                        context["message"] = "Votre mot de passe doit contenir 8 caractères"
                        context["color"] = "red"

    return render(request, 'account/create_account.html', context)


def my_account(request):
    context = {}

    return render(request, 'account/my_account.html', context)
