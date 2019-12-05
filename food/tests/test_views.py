#! /usr/bin/env python3
# coding: UTF-8

""" TestViews class """


# imports
from unittest import TestCase
from food.models import Food
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """ TestViews class :
    test_add_favorites method
    test_delete_favorites method
    """

    def setUp(self):
        self.user = get_user_model()
        self.user.objects.create_user(id='1', username='Null', email='test@test1.fr', password='testtest')
        self.id_user = 1
        self.id_food = 1

    def test_add_favorites(self):
        # add favorites
        food = Food.objects.get(id=self.id_food)
        user = self.user.objects.get(id=self.id_user)
        food.favorites.add(user)

        # try to get the favorites data
        try:
            self.user(id=self.id_user).food_set.get(id=self.id_food)
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertTrue(data)

        try:
            self.user(id=self.id_user).food_set.get(id=2)
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertFalse(data)

    def test_delete_favorites(self):
        # delete favorites
        food = Food.objects.get(id=self.id_food)
        user = self.user.objects.get(id=self.id_user)
        food.favorites.remove(user)

        # try to get the favorites data
        try:
            self.user(id=self.id_user).food_set.get(id=self.id_user)
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertFalse(data)
