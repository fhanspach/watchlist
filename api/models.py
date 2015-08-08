from django.db import models
from django.utils.safestring import mark_safe
import math


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

    def __str__(self):
        return "{} ({})".format(self.title, self.release.year)

    def get_poster_html(self):
        return mark_safe("<img src='{}' height=180/>".format(self.poster))

    def get_poster_small_html(self):
        return mark_safe("<a href='/admin/api/movie/{}/'><img src='{}' height=80/></a>".format(self.pk, self.poster))

    def get_url(self):
        # FIXME this is not generic
        return "/admin/api/movie/{}/'".format(self.pk)

    def get_html_stars(self):
        result = ""
        rating = self.imdb_score / 2
        int_part = math.floor(rating)
        for i in range(0, int_part):
            result += "<span class='fa fa-star'></span>"
        if (rating - int_part) >= 0.5:
            result += "<span class='fa fa-star-half-o'></span>"
        else:
            result += "<span class='fa fa-star-o'></span>"
        for i in range(1, 5 - int_part):
            result += "<span class='fa fa-star-o'></span>"
        return mark_safe(result)


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_movies_display(self):
        result = ""
        for movie in self.movie_set.all():
            result += "{}".format(movie.get_poster_small_html())
        return mark_safe(result)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_movies_display(self):
        result = ""
        for movie in self.directed_movies.all():
            result += "{}".format(movie.get_poster_small_html())
        for movie in self.acted_movies.all():
            result += "{}".format(movie.get_poster_small_html())
        return mark_safe(result)
