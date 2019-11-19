#! /usr/bin/env python3
# coding: UTF-8

""" Views of the food application """


# imports
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from food.classes import database
from food.models import Food, Categorie
from account.forms import Account

from requests.exceptions import ConnectionError
from django.db.utils import IntegrityError
from django.contrib.auth import logout
from django.contrib.auth import get_user_model




def index(request):
    # USER'S DISCONNECTION
    if request.method == 'POST':
        # get disconnection == 'True' if user clicked to the exit logo
        disconnection = request.POST.get('disconnection', 'False')
        if request.user.is_authenticated and disconnection == 'True':
            logout(request)
            context = {'message': "Vous êtes bien déconnecté."}
            return render(request, 'food/index.html', context)

    # INSERT DATA IF THE DATABASE IS EMPTY
    try:
        bdd = database.Database()
        bdd.insert_data()
        return render(request, 'food/index.html')
    except ConnectionError:
        context = {'message': "Problème de connexion"}
        return render(request, 'food/index.html', context)


def result(request):
    if request.method == 'POST':
        # get the id food selected by the user
        save_id_food = request.POST.get('id', None)
        print(save_id_food, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        if save_id_food:
            # SAVE FOOD SELECTED BY USER
            # if user is authenticated
            if request.user.is_authenticated:
                print('authentifié')
                id_user = 1
                food = Food.objects.get(id=save_id_food)
                user = get_user_model()
                user = user.objects.get(id=id_user)
                food.favorites.add(user)

            # DISPLAY ACCESS_ACCOUNT PAGE
            # if user is not authenticated
            if not request.user.is_authenticated:
                print("non authentifié")
                form = Account()
                message = ["Veuillez vous connecter pour accéder à vos favoris."]
                context = {'form': form, 'message': message, 'color': 'red'}
                return render(request, 'account/access_account.html', context)

        if save_id_food is None:
            # get the name food searched
            food = request.POST.get('search')
            print(food)

            # DISPLAY THE INDEX PAGE WITH AN ERROR MESSAGE
            # if there is no food searched
            if not food:
                context = {'message': "Vous n'avez rien demandé"}
                print(context)
                return render(request, 'food/index.html', context)

            # if there is food searched
            else:
                context = {}
                context['search'] = food
                # get the categorie of the food searched
                list_food = food.split()
                for word in list_food:
                    name = Food.objects.filter(name__icontains=word)[:1]
                    categorie_food = name.values_list('categorie')

                    # DISPLAY THE RESULT PAGE
                    # if a categorie exists
                    if categorie_food:
                        # get data of all foods of the same categorie
                        # ordered by nutrition grade
                        context = {}
                        categorie_food = categorie_food[0]
                        data = Food.objects.filter(categorie=categorie_food)
                        foods_data = data.order_by('nutrition_grade')
                        context['foods_data'] = foods_data

                        # does not display the floppy logo
                        # if the user has already registered the food
                        if request.user.is_authenticated:
                            # get the favorites foods id
                            user = get_user_model()
                            favorites_id = []
                            for elt in user(id=1).food_set.values_list('id'):
                                favorites_id.append(elt[0])
                            context['authenticated'] = 'True'
                            context['favorites_id'] = favorites_id
                        else:
                            context['authenticated'] = 'False'
                            context['favorites_id'] = []

                        return render(request, 'food/result.html', context)

                    # DISPLAY THE INDEX PAGE WITH AN ERROR MESSAGE
                    # if a categorie don't exists
                    else:
                        # create context dictionary
                        context = {"message": "Pas de résultat."}
                        return render(request, 'food/index.html', context)


def detail(request):
    # DISPLAY THE DETAIL PAGE
    if request.method == 'POST':
        # get id of the food selected
        id_food = request.POST.get('id_food', None)

        # get the data to the food selected
        food = Food.objects.values_list('name', 'nutrition_grade', 'url_picture', 'link', 'energy',
                                        'proteins', 'fat', 'carbohydrates', 'sugars', 'fiber', 'sodium')
        food_data = food.get(id=id_food)

        # create the context dictionary
        context = {}
        name_data = ('name', 'nutrition_grade', 'url_picture', 'link', 'energy', 'proteins', 'fat',
                     'carbohydrates', 'sugars', 'fiber', 'sodium')
        for i, elt in enumerate(name_data):
            context[elt] = food_data[i]

        return render(request, 'food/detail.html', context)


def favorites(request):
    # DELETE THE FOOD SELECTED BY USER
    if request.method == 'POST':
        id_food = request.POST.get('id', None)
        id_user = 1
        food = Food.objects.get(id=id_food)
        user = get_user_model()
        user = user.objects.get(id=id_user)
        food.favorites.remove(user)

    # RETURN TO THE ACCESS_ACCOUNT PAGE
    # if user is not authenticated
    if not request.user.is_authenticated:
        # redirect to the access_account page
        form = Account()
        message = ["Veuillez vous connecter pour accéder à vos favoris."]
        context = {'form': form, 'message': message, 'color': 'red'}
        return render(request, 'account/access_account.html', context)

    # DISPLAY THE FAVORITES PAGE
    # if user is authenticated
    else:
        # get the favorites food data
        user = get_user_model()
        data = user(id=1).food_set.all()
        # create context dictionary
        context = {'data': data}
        return render(request, 'food/favorites.html', context)
