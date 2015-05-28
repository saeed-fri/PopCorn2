from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=60)
    summery = models.TextField()
    rating_sum = models.BigIntegerField(default=0)
    rating_count = models.BigIntegerField(default=0)
    imdb = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Cast(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    movie = models.ForeignKey(Movie)


    def __str__(self):
        return self.name


class Crew(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    role = models.CharField(max_length=60)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.name