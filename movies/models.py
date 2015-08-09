import uuid
from django.db import models

from django.utils.safestring import mark_safe
import math
from api.models import Movie


class Watchlist(models.Model):
    title = models.CharField(max_length=255)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.title)

    @property
    def get_movies_html(self):
        list_elements = ""
        for watchlist_movie in WatchlistMovie.objects.filter(watchlist=self):
            list_elements += "<li style='{}'><a href='{}'>{}</a></li>".format(
                "text-decoration: line-through;" if watchlist_movie.seen else "",
                watchlist_movie.movie.get_url(),
                watchlist_movie.movie)
        result = "<ul>{}</ul>".format(list_elements)
        return mark_safe(result)

    @property
    def get_progress_html(self):
        # FIXME this method is only usable if it's more generic
        list_elements = ""
        movies = WatchlistMovie.objects.filter(watchlist=self).order_by("seen")
        percentage = 100 / movies.count()
        for watchlist_movie in movies:
            list_elements += "<div style='width:{}%; height:5px; background-color:{}; float:left;'></div>".format(
                percentage,
                '#2cc36b' if watchlist_movie.seen else "#c0392b")
        result = "<div style='height:20px; width:200px'>{}</div>".format(list_elements)
        return mark_safe(result)


class WatchlistMovie(models.Model):
    movie = models.ForeignKey(Movie)
    watchlist = models.ForeignKey("Watchlist")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.movie)
