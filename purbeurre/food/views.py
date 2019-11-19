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
    # user's disconnection
    if request.method == 'POST':
        disconnection = request.POST.get('disconnection', 'False')
        if disconnection == 'True' and request.user.is_authenticated:
            logout(request)
            context = {'message': "Vous êtes bien déconnecté."}
            return render(request, 'food/index.html', context)

    # insert data if database is empty
    try:
        bdd = database.Database()
        bdd.insert_data()
        return render(request, 'food/index.html')
    except ConnectionError:
        context = {'message': "Problème de connexion"}
        return render(request, 'food/index.html', context)




def result(request):
    if request.method == 'POST':

        # SAVE FOOD SELECTED BY USER
        save_id_food = request.POST.get('id', None)
        id_user = 1
        print(save_id_food, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

        if save_id_food:
            if request.user.is_authenticated:
                print('authentifié')
                # ENREGISTRER DANS COURS L'INSERTION DES DONNEES DANS TABLE INTERMEDIAIRE

                food = Food.objects.get(id=save_id_food)
                user = get_user_model()
                user = user.objects.get(id=id_user)
                try:
                    food.favorites.add(user)
                except IntegrityError:
                    pass
                return render(request, 'account/access_account.html')

            if not request.user.is_authenticated:
                # redirect to the access_account page
                form = Account()
                message = ["Veuillez vous connecter pour accéder à vos favoris."]
                context = {'form': form, 'message': message, 'color': 'red'}
                print("non authentifié")
                return render(request, 'account/access_account.html', context)

        if save_id_food is None:
            # DISPLAY AN ERROR MESSAGE OR RETURN THE RESULT PAGE
            # get food searched
            food = request.POST.get('search')
            print(food)
            # if there is no food searched
            if not food:
                # create context dictionary
                context = {'message': "Vous n'avez rien demandé"}
                print(context)
                return render(request, 'food/index.html', context)

            # if there is food searched
            else:
                print('suite')
                # get the categorie of the food searched in the database
                list_food = food.split()
                for word in list_food:
                    name = Food.objects.filter(name__icontains=word)[:1]
                    categorie_food = name.values_list('categorie')

                    # if a categorie exists
                    if categorie_food:
                        # get data of all foods of the same categorie and order by nutrition grade
                        categorie_food = categorie_food[0]
                        data = Food.objects.filter(categorie=categorie_food)
                        foods_data = data.order_by('nutrition_grade')

                        # get the favorites foods id
                        user = get_user_model()
                        favorites_id = []
                        for elt in user(id=1).food_set.values_list('id'):
                            favorites_id.append(elt[0])
                        print(favorites_id)

                        # create context dictionary
                        context = {'search': food, 'foods_data': foods_data, 'favorites_id': favorites_id, 'authenticated': 'False'}
                        return render(request, 'food/result.html', context)

                    # if a categorie don't exists
                    else:
                        # create context dictionary
                        context = {"message": "Pas de résultat."}
                        return render(request, 'food/index.html', context)



def detail(request):
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
    # if user is not authenticated
    if not request.user.is_authenticated:
        # redirect to the access_account page
        form = Account()
        message = ["Veuillez vous connecter pour accéder à vos favoris."]
        context = {'form': form, 'message': message, 'color': 'red'}
        return render(request, 'account/access_account.html', context)

    # if user is authenticated
    else:
        # get the favorites food data
        user = get_user_model()
        data = user(id=1).food_set.all()

        # create context dictionary
        context = {'data': data}

        return render(request, 'food/favorites.html', context)
