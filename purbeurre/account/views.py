#! /usr/bin/env python3
# coding: UTF-8

""" Views """


# Imports
from django.shortcuts import render, redirect
import re
from account.forms import CreateAccount, AccessAccount
from account.models import User
import hashlib






def access_account(request):
    form = AccessAccount()
    context = {'form': form}

    if request.method == 'GET':
        form = AccessAccount(request.GET)

        # if the data entered by the user is valid
        if form.is_valid() is True or 'e_mail' in form.errors.as_data():

            # if e-mail is valid
            email = str(request.GET.get('e_mail'))
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is not None:

                # if user's e-mail exists to the database
                data = User.objects.values_list('e_mail')
                for elt in data:
                    elt = elt[0]
                    if email == elt :
                        # encrypted user's password
                        password = request.GET.get('password')
                        password = password.encode()
                        encrypted_password = hashlib.sha1(password).hexdigest()
                        # get password encrypted to the databse
                        data = User.objects.values_list('password')
                        password_database = str(data.get(e_mail=email)[0])

                        # if the user's password ok
                        if password_database == encrypted_password:
                            csrf = request.GET.get('csrfmiddlewaretoken')
                            mail = request.GET.get('e_mail')
                            password = request.GET.get('password')

                            # redirected from my account page
                            return redirect('/account/my_account/?csrfmiddlewaretoken='+csrf+'&e_mail='+mail+'&password='+password)

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
            email = str(request.GET.get('e_mail'))
            regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"
            if re.match(regexp, email) is None:
                context["message"] = "L'e-mail n'est pas valide."
                context["color"] = "red"

            # if e-mail is valid
            else:
                password = request.GET.get('password')
                # if user's password is too long
                if len(password) > 8:
                    context["message"] = "Votre mot de passe doit contenir 8 caractères"
                    context["color"] = "red"

    return render(request, 'account/access_account.html', context)



def create_account(request):
    form = CreateAccount()
    context = {'form': form}

    if request.method == 'POST':
        form = CreateAccount(request.POST)

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
                # if user's e-mail exists to the database
                email_database = str(User.objects.get(e_mail__icontains=email))
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

    return render(request, 'account/my_account.html')
