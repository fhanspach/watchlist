from django.db import models
from django.utils.safestring import mark_safe


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


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


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
