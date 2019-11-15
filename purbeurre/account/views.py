#! /usr/bin/env python3
# coding: UTF-8

""" Views """


# Imports
from django.shortcuts import render
from account.forms import Account
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login



def access_account(request):
    form = Account()
    context = {'form': form}

    if request.method == 'POST':
        form = Account(request.POST)
        # get the user's data
        email = request.POST.get('email')
        password = request.POST.get('password')
        # verify that the user exists
        user = authenticate(email=email, password=password)

        # if user exists - connection and confirmation message
        if user:
           login(request, user)
           context["message"] = ["Vous êtes connecté."]
           context["color"] = "green"

        elif not user:
            if form.is_valid() is False:
                # add the error messages in the context dictionary
                error_list = []
                for key, value in form.errors.as_data().items():
                    message = str(key).title() + ' : ' + str(value[0]).replace("['", "").replace("']", "")
                    error_list.append(message)
                    context["message"] = error_list
                    context["color"] = "red"
            else:
                # add the error message in the context dictionary
                context["message"] = ["Ce compte n'existe pas."]
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
