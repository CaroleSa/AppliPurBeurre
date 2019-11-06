#! /usr/bin/env python3
# coding: UTF-8

""" Models """


# Import
from django.db import models
from django.utils import timezone



class User(models.Model):
    e_mail = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)
