from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=511)
    release = models.DateField()
    rating = models.CharField(max_length=15)
    runtime = models.IntegerField()
    genre = models.ManyToManyField("Genre")
    director = models.ManyToManyField("Person", related_name="directed_movies")
    actors = models.ManyToManyField("Person", related_name="acted_movies")
    writer = models.CharField(max_length=1023)
    plot = models.TextField()
    country = models.CharField(max_length=127)
    poster = models.URLField()
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)


class Genre(models.Model):
    title = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=128)
