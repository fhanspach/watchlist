import uuid
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from api.models import Movie


class Watchlist(models.Model):
    title = models.CharField(max_length=255)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return "{}".format(self.title)

    @property
    def get_movies_html(self):
        list_elements = ""
        for watchlist_movie in WatchlistMovie.objects.filter(watchlist=self):
            list_elements += "<li>{}</li>".format(watchlist_movie.movie)
        result = "<ul>{}</ul>".format(list_elements)
        return mark_safe(result)


class WatchlistMovie(models.Model):
    movie = models.ForeignKey(Movie)
    watchlist = models.ForeignKey("Watchlist")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.movie)
