#! /usr/bin/env python3
# coding: UTF-8

""" Views of the food application """


# imports
from django.shortcuts import render
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
        context = {'error': "Problème de connexion"}
        return render(request, 'food/index.html', context)


def result(request):
    # get food searched
    food = "Nutella"

    # get food categorie
    data = Food.objects.values_list('categorie')
    categorie_food = data.get(name=food)

    # get data of all foods of the same categorie
    data = Food.objects.values_list('name', 'nutrition_grade', 'url_picture')
    foods_data = data.filter(categorie=categorie_food)

    # create context dictionary
    context = {'foods_data': foods_data}

    # save favorite food
    save_favorite = False
    food_saved = "Nutella"
    if save_favorite == True:
        id_foods = Food.objects.values_list('id')
        id_food = id_foods.get(name=food_saved)
        Favorite.food.create(food=id_food)

    return render(request, 'food/result.html', context)


def detail(request):
    # get food selected
    food = "Nutella"

    # create context dictionary
    context = {}

    # create a list that contains the data to retrieve
    list = ['energy', 'proteins', 'fat', 'carbohydrates', 'sugars', 'fiber', 'sodium', 'url_picture', 'link']
    for elt in list:
        # get data in the database
        data = Food.objects.values_list(elt)
        data_food = data.get(name=food)
        # insert data in context dictionary
        context[elt] = data_food[0]

    return render(request, 'food/detail.html', context)


def favorites(request):
    id_favorites_foods = Favorite.objects.values_list('id')
    for id in id_favorites_foods:
        data = Food.filter(id=id)
        data_foods = data.values_list('name', 'link', 'url_picture')
        print("TTEESSTT", data_foods[0])
        # insert data in context dictionary



    return render(request, 'food/favorites.html')