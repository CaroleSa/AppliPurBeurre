#! /usr/bin/env python3
# coding: UTF-8

""" Class Database """



# imports
import psycopg2
from purbeurre.purbeurre.settings import DATABASES
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


        for elt, data in zip(categories_food, list_data):

            # inserting data into Food table
            for value in data['products']:

                product_name = "\'" + value['product_name_fr'].replace("'", "") + "\'"
                nutrition_grade = "\'" + value['nutrition_grade_fr'].replace("'", "") + "\'"
                nutriments = value['nutriments']
                picture = "\'" + value['image_url'].replace("'", "") + "\'"
                url = "\'" + value['url'].replace("'", "") + "\'"

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
                    print(product_name, name, value)







# instantiate the class Database
NEW_DATABASE = InsertData()
NEW_DATABASE.test()
