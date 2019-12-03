#! /usr/bin/env python3
# coding: UTF-8

""" TestDatabase class """


# imports
from unittest import TestCase
from unittest.mock import patch
from food.models import Food





class TestDatabase(TestCase):
    """ TestDatabase class :
    test_get_data method """


    def test_data_database_exists(self):
        """ Verify that the method insert the data """

        self.assertTrue(Food.objects.all().exists())


