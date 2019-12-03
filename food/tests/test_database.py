#! /usr/bin/env python3
# coding: UTF-8

""" TestDatabase class """


# imports
from unittest import TestCase
from food.models import Food, Categorie


class TestDatabase(TestCase):
    """ TestDatabase class :
    test_food_data_exists method
    test_categorie_data_exists method"""

    def test_categorie_data_exists(self):
        """ Verify that the method insert the categorie data """
        self.assertTrue(Categorie.objects.all().exists())

    def test_food_data_exists(self):
        """ Verify that the method insert the food data """
        self.assertTrue(Food.objects.all().exists())
