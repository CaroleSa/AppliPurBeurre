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

        # creating an empty list
        self.list_data = []

    def load_data(self):
        """ Loading data of the A.P.I. Open Food Facts and convert to json """
        # creating the list that contains foods data of categories chooses
        for elt in self.categories:
            payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': "\'" + elt + "\'", 'sort_by': 'unique_scans_n', 'page_size': 100,
                       'axis_x': 'energy', 'axis_y': 'products_n', 'json': '1'}
            request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
            data = request.json()
            self.list_data.append(data)

        return self.list_data
