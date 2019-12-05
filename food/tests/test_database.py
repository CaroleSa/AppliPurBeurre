#! /usr/bin/env python3
# coding: UTF-8

""" TestDatabase class """


# imports
from unittest import TestCase
from food.models import Food, Categorie


class TestDatabase(TestCase):
    """ TestDatabase class :
    test_food_data_exists method
    test_categorie_data_exists method
    test_food_name_exists method
    test_categorie_name_exists method """

    def test_categorie_data_exists(self):
        """ Verify that the database contains the categorie data """
        self.assertTrue(Categorie.objects.all().exists())

    def test_food_data_exists(self):
        """ Verify that the database contains the food data """
        self.assertTrue(Food.objects.all().exists())

    def test_food_name_exists(self):
        """ Verify that the Food table contains the name : Pizza Cuite sur Pierre (Bolognese) """
        try:
            Food.objects.get(name="Pizza Cuite sur Pierre (Bolognese)")
            name = True
        except Food.DoesNotExist:
            name = False
        self.assertTrue(name)

    def test_categorie_name_exists(self):
        """ Verify that the Categorie table contains the name : pizza """
        try:
            Categorie.objects.get(name="pizza")
            name = True
        except Categorie.DoesNotExist:
            name = False
        self.assertTrue(name)
