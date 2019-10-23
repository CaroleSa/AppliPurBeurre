#! /usr/bin/env python3
# coding: UTF-8

""" Class Database """

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'purbeurre.purbeurre.settings'

import django
django.setup()

# imports
import psycopg2
from purbeurre.settings import DATABASES
from food.models import Food, Categorie
from food.classes.call_api import CallApi
import django.db




class Database:

    def __init__(self):

        # instantiate the class Call_api
        self.new_call_api = CallApi()

    def insert_data(self):
        # insert the data if they do not exist in the database
        # get categories list and the data food of the CallApi class
        categories_food = self.new_call_api.categories
        list_data = self.new_call_api.load_data()

        for elt, data in zip(categories_food, list_data):

            try :
                # insert data in Categorie table
                # index = categories_food.index(elt)
                index = categories_food.index(elt) + 1
                Categorie.objects.create(name=elt)

                for value in data['products']:

                    # get data product_name, nutrition_grade, ...
                    product_name = value['product_name_fr']
                    grade = value['nutrition_grade_fr']
                    picture = value['image_url']
                    page_link = value['url']
                    nutriments = value['nutriments']
                    energy_100g = nutriments.get('energy_100g')
                    proteins_100g = nutriments.get('proteins_100g')
                    fat_100g = nutriments.get('fat_100g')
                    carbohydrates_100g = nutriments.get('carbohydrates_100g')
                    sugars_100g = nutriments.get('sugars_100g')
                    fiber_100g = nutriments.get('fiber_100g')
                    sodium_100g = nutriments.get('sodium_100g')

                    categorie_id = Categorie.objects.get(id=index)

                    # inserting data in Food table
                    Food.objects.create(name=product_name, categorie=categorie_id,
                                        nutrition_grade=grade, url_picture=picture, link=page_link,
                                        energy=energy_100g, proteins=proteins_100g, fat=fat_100g,
                                        carbohydrates=carbohydrates_100g, sugars=sugars_100g, fiber=fiber_100g,
                                        sodium=sodium_100g)

            except django.db.utils.IntegrityError:
                continue
