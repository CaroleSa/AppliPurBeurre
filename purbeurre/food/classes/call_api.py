#! /usr/bin/env python3
# coding: UTF-8

""" Class CallApi """



# import
import requests



class CallApi:
    """ Call A.P.I. OpenFoodFacts """

    def __init__(self):
        # creating categories food list used in the program
        self.categories = ['pizza', 'pate a tartiner', 'gateau', 'yaourt', 'bonbon']

        self.page_number = 2
        # creating an empty list
        self.list_data = []

    def load_data(self):
        """ Loading data of the A.P.I. Open Food Facts and convert to json """
        # creating the list that contains foods data of categories chooses
        for elt in self.categories:
            payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': "\'" + elt + "\'", 'sort_by': 'unique_scans_n', 'page_size': self.page_number,
                       'axis_x': 'energy', 'axis_y': 'products_n', 'json': '1'}
            request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
            data = request.json()

            self.list_data.append(data)

        """for data in self.list_data:

            index = self.list_data.index(data)
            print(index)

            for value in data['products']:
                index_2 = len(data['products'])
                print(index_2)


                product_name = "\'" + value['product_name_fr'].replace("'", "") + "\'"
                nutrition_grade = "\'" + value['nutrition_grade_fr'].replace("'", "") + "\'"
                picture = "\'" + value['image_url'].replace("'", "") + "\'"
                link = "\'" + value['url'].replace("'", "") + "\'"

                nutriments = value['nutriments']
                energy = "\'" + str(nutriments.get('energy_100g')) + "\'"
                proteins = "\'" + str(nutriments.get('proteins_100g')) + "\'"
                fat = "\'" + str(nutriments.get('fat_100g')) + "\'"
                carbohydrates = "\'" + str(nutriments.get('carbohydrates_100g')) + "\'"
                sugars = "\'" + str(nutriments.get('sugars_100g')) + "\'"
                fiber = "\'" + str(nutriments.get('fiber_100g')) + "\'"

                sodium = "\'" + str(nutriments.get('sodium_100g')) + "\'" """



        return self.list_data

"""nex = CallApi()
nex.load_data()"""
