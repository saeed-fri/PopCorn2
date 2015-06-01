from django.db import models
from django.contrib.auth.models import User

"""
class User(models.Model):
    username = models.CharField(max_length=30)
    alias = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    birthday = models.DateTimeField()
"""

class UserProfile(models.Model):  #SiteUser is an extension of User
    user = models.OneToOneField(User)
    alias = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return str(self.user)