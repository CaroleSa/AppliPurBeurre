#! /usr/bin/env python3
# coding: UTF-8

""" Models """


# Import
from django.db import models



class Nutriment(models.Model):
    energy = models.DecimalField(max_digits=5, decimal_places=1)
    proteins = models.DecimalField(max_digits=4, decimal_places=1)
    fat = models.DecimalField(max_digits=4, decimal_places=1)
    satured_fat = models.DecimalField(max_digits=3, decimal_places=1)
    carbohydrates = models.DecimalField(max_digits=4, decimal_places=1)
    sugars = models.DecimalField(max_digits=4, decimal_places=1)
    fiber = models.DecimalField(max_digits=3, decimal_places=1)
    sodium = models.DecimalField(max_digits=4, decimal_places=1)

class Categorie(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Food(models.Model):
    name = models.CharField(max_length=120, unique=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nutriment = models.OneToOneField(Nutriment, on_delete=models.CASCADE)
    nutrition_grade = models.CharField(max_length=1)
    url_picture = models.URLField(unique=True)
    link = models.URLField(unique=True)

class Favorite(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
