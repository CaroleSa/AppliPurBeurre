#! /usr/bin/env python3
# coding: UTF-8

""" Models """

# Import
from django.contrib.auth.models import AbstractUser
from food.models import Food
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    e_mail = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)
    favorites = models.ManyToManyField(Food)

    def __str__(self):
        return self.e_mail, self.creation_date, self.favorites