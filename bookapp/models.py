from operator import mod
from unicodedata import category
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailId = models.EmailField(unique=True)
    role = models.CharField(max_length=100)
    lastLogin = models.DateTimeField()
    password = models.CharField(max_length=100, default='pass')
    
    def __str__(self):
        return self.firstName


class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="Horro")

    def __str__(self):
        return self.name
