#! /usr/bin/env python3
# coding: UTF-8

""" Class Database """



# imports
import psycopg2
from purbeurre.purbeurre.settings import DATABASES
from purbeurre.food.models import Food, Nutriment, Categorie
from purbeurre.food.classes.call_api import CallApi




class InsertData:
    """ Creation database and insert data """

    def __init__(self):
        """ Connection at MySQL and creation of cursor """
        """"# connection at PostgreSql and creation cursor
        default = DATABASES.get("default")
        user = default.get("USER")
        name_bdd = default.get("NAME")
        conn = psycopg2.connect("dbname={} user={}".format(name_bdd, user))

        self.cursor = conn.cursor()"""

        # instantiate the class Call_api
        self.new_call_api = CallApi()


    def test(self):

        # get attributes of CallApi class
        categories_food = self.new_call_api.categories
        list_data = self.new_call_api.load_data()
        i=0
        # METTRE CONDITION + EXCEPT
        for elt, data in zip(categories_food, list_data):

            # inserting data into Food table
            for value in data['products']:

                product_name = "\'" + value['product_name_fr'].replace("'", "") + "\'"
                nutrition_grade = "\'" + value['nutrition_grade_fr'].replace("'", "") + "\'"
                nutriments = value['nutriments']
                picture = "\'" + value['image_url'].replace("'", "") + "\'"
                link = "\'" + value['url'].replace("'", "") + "\'"

                # insert data to the database (Categorie table)
                Categorie.objects.create(name=elt)
                categorie_id = Categorie.objects.values_list('ID').filter(name=elt)

                # insert data to the database (Food table)
                Food.objects.create(name=product_name)
                Food.objects.create(categorie=categorie_id)
                Food.objects.create(nutriment=i)
                Food.objects.create(nutrition_grade=nutrition_grade)
                Food.objects.create(utl_picture=picture)
                Food.objects.create(link=link)
                i += 1

                nutriments_name = ["energy", "proteins", "fat", "satured-fat", "carbohydrates", "sugars",
                                   "fiber", "sodium"]

                for name in nutriments_name:
                    # string concatenation
                    name_100 = name + "_100g"
                    # get nutriments value in API
                    value = nutriments.get(name_100)
                    if value == None:
                        value = "NULL"
                    name = "\'" + name.replace("'", "") + "\'"
                    name = name.replace("-", "_")
                    print(product_name, name, value)

                    # insert data to the database (Nutriment table)
                    Nutriment.objects.create(name=value)







# instantiate the class Database
NEW_DATABASE = InsertData()
NEW_DATABASE.test()
