from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=30)
    alias = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    birthday = models.DateTimeField()