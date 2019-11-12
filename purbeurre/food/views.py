#! /usr/bin/env python3
# coding: UTF-8

""" Views of the food application """


# imports
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from food.classes import database
from food.models import Food, Categorie
from account.models import UserAccount
from requests.exceptions import ConnectionError
from django.db.utils import IntegrityError
from django.db.models import F


def index(request):
    # create database and insert data if database is empty
    try:
        bdd = database.Database()
        bdd.insert_data()
        return render(request, 'food/index.html')
    except ConnectionError:
        context = {'error_message': "Problème de connexion"}
        return render(request, 'food/index.html', context)



def result(request):
    # cette ligne inutile ?
    if request.method == 'POST':
        # SAVE FOOD SELECTED BY USER
        id_food = request.POST.get('id', None)
        # ON TESTE JUSTE LE USER 1
        id_user = 1
        if id_food and id_user is not None:
            # ENREGISTRER DANS COURS L'INSERTION DES DONNEES DANS TABLE INTERMEDIAIRE
            food = Food.objects.get(id=id_food)
            user = UserAccount.objects.get(id=id_user)
            try:
                user.favorites.add(food)
            except IntegrityError:
                pass

        # DISPLAY AN ERROR MESSAGE OR RETURN THE RESULT PAGE
        # get food searched
        food = request.POST.get('search')

        # if there is no food searched
        if not food:
            # create context dictionary
            context = {'message': "Vous n'avez rien demandé"}
            return render(request, 'food/index.html', context)

        # if there is food searched
        else:
            # get the categorie of the food searched in the database
            list_food = food.split()
            for word in list_food:
                name = Food.objects.filter(name__icontains=word)[ :1]
                categorie_food = name.values_list('categorie')

                # if a categorie exists
                if categorie_food:
                    # get data of all foods of the same categorie and order by nutrition grade
                    categorie_food = categorie_food[0]
                    data = Food.objects.filter(categorie=categorie_food)
                    foods_data = data.order_by('nutrition_grade')

                    # create context dictionary
                    context = {'search': food, 'foods_data': foods_data}
                    return render(request, 'food/result.html', context)

                # if a categorie don't exists
                else:
                    # create context dictionary
                    context = {"message": "Pas de résultat."}
                    return render(request, 'food/result.html', context)



def detail(request):

    if request.method == 'POST':
        id_food = request.POST.get('id_food', None)
        print(id_food, "detailFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

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

        data = Food.objects.filter(useraccount__id=1)

        context = {'data': data}

        return render(request, 'food/favorites.html', context)
