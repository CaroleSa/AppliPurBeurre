#! /usr/bin/env python3
# coding: UTF-8

""" Views """


# Imports
from django.shortcuts import render, redirect
import re
from account.forms import Account

import hashlib
from django.contrib.auth import get_user_model






def access_account(request):
    form = Account()
    context = {'form': form}
    user = get_user_model()

    if request.method == 'POST':
        form = Account(request.POST)

        error_message = str(form.errors.as_data()['email'][0])
        email_exists = "['Un objet Utilisateur avec ce champ Adresse électronique existe déjà.']"

        # if the data entered by the user is valid
        if form.is_valid() is True or error_message == email_exists:
            print(error_message, "marcheLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

            # if e-mail is valid
            email = str(request.POST.get('e_mail'))
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is not None:

                # if user's e-mail exists to the database
                data = user.objects.values_list('e_mail')
                for elt in data:
                    elt = elt[0]
                    if email == elt:
                        # encrypted user's password
                        password = request.POST.get('password')
                        password = password.encode()
                        encrypted_password = hashlib.sha1(password).hexdigest()
                        # get password encrypted to the databse
                        data = user.objects.values_list('password')
                        password_database = str(data.get(e_mail=email)[0])

                        # if the user's password ok, return my_account page
                        if password_database == encrypted_password:
                            data = user.objects.values_list('creation_date')
                            date = data.get(e_mail=email)[0]
                            context = {'date': date, 'mail': email}
                            return render(request, 'account/my_account.html', context)

                        # if the user's password don't ok
                        else:
                            context["message"] = "Le compte existe mais le mot de passe n'est pas valide."
                            context["color"] = "red"

                    # if user's e-mail don't exists to the database
                    else:
                        context["message"] = "Ce compte n'existe pas."
                        context["color"] = "red"

            # if e-mail isn't valid
            else:
                if len(email) >= 6:
                    context["message"] = "L'e-mail n'est pas valide."
                    context["color"] = "red"

        # if the data entered by the user is not valid
        else:
            # if e-mail is not valid
            email = str(request.POST.get('e_mail'))
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is None:
                context["message"] = "L'e-mail n'est pas valide."
                context["color"] = "red"

            # if e-mail is valid
            else:
                password = request.POST.get('password')
                # if user's password is too long
                if len(password) > 8:
                    context["message"] = "Votre mot de passe doit contenir 8 caractères"
                    context["color"] = "red"

    return render(request, 'account/access_account.html', context)



def create_account(request):
    user = get_user_model()
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        form = Account(request.POST)
        # get user's data
        email = request.POST.get('email')
        password_control = request.POST.get('passwordControl')
        password = request.POST.get('password')

        # if the data entered by the user is valid
        if form.is_valid() is True:

            # if password and password control are the same
            if password_control == password:
                user.objects.create_user(username='Null', email=email, password=password)
                context["message"] = ["Votre compte a bien été créé."]
                context["color"] = "green"

            # if password and password control aren't the same
            else:
                # create error message
                context["message"] = ["Vos mots de passe ne sont pas identiques."]
                context["color"] = "red"

        else:
            # add the error messages in the context dictionary
            error_list = []
            for key, value in form.errors.as_data().items():
                message = str(key).title() + ' : ' + str(value[0]).replace("['", "").replace("']", "")
                error_list.append(message)
                context["message"] = error_list
                context["color"] = "red"

    return render(request, 'account/create_account.html', context)
