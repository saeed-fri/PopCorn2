from django.db import models
from User.models import UserProfile
from Movie.models import Movie


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    movie = models.ForeignKey(Movie)
    text = models.TextField()
    rate = models.SmallIntegerField(range(0, 5))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' : ' + str(self.movie) + ' : ' + str(self.rate)
