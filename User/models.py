from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):  #UserProfile is an extension of User
    user = models.OneToOneField(User)
    alias = models.CharField(max_length=50)
    birthday = models.DateField()
    #image = models.ImageField()
    #follows = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return str(self.user)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follower')
    followee = models.ForeignKey(UserProfile, related_name='followee')