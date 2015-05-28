from django.db import models


class movie(models.Model):
    name = models.CharField(max_length=60)
    summery = models.TextField()
    rating_sum = models.BigIntegerField(default=0)
    rating_count = models.BigIntegerField(default=0)
    imdb = models.CharField(max_length=50)
