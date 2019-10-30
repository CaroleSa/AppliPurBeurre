#! /usr/bin/env python3
# coding: UTF-8

""" Views of the food application """


# imports
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from food.classes import database
from food.models import Food, Categorie, Favorite
from requests.exceptions import ConnectionError


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

    # get food searched
    food = request.GET.get('search')

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
                return render(request, 'food/index.html', context)


    # save favorite food
    save_favorite = False
    food_saved = "Nutella"
    if save_favorite == True:
        id_foods = Food.objects.values_list('id')
        id_food = id_foods.get(name=food_saved)
        Favorite.food.create(food=id_food)


def detail(request):
    # get food selected
    #food = request.GET.get('e_mail')
    context = {}

    """# create a list that contains the data to retrieve
    list = ['energy', 'proteins', 'fat', 'carbohydrates', 'sugars', 'fiber', 'sodium', 'url_picture', 'link']
    for elt in list:
        # get data in the database
        data = Food.objects.values_list(elt)
        data_food = data.get(name=food)
        # insert data in context dictionary
        context[elt] = data_food[0]"""

    return render(request, 'food/detail.html', context)


def favorites(request):
    id_favorites_foods = Favorite.objects.values_list('id')
    for id in id_favorites_foods:
        data = Food.filter(id=id)
        data_foods = data.values_list('name', 'link', 'url_picture')
        print("TTEESSTT", data_foods[0])
        # insert data in context dictionary



    return render(request, 'food/favorites.html')