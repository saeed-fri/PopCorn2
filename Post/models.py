from django.db import models
from User.models import UserProfile
from Movie.models import Movie


class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    movie = models.ForeignKey(Movie)
    text = models.TextField()
    rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.author) + ' : ' + str(self.movie) + ' : ' + str(self.rate)


class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(UserProfile)

    def __str__(self):
        return str(self.user) + " liked " + str(self.post)


class Comment(models.Model):
    author = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)
    text = models.TextField()

    def __str__(self):
        return str(self.author) + " commented on " + str(self.post)