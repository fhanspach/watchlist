import uuid
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe
from api.models import Movie
from movies.models import Watchlist

def all_movies(request):
    return render_list(Movie.objects.all(), request, None, template="ui/movies_thumbnail.html")

def render_list(movies, request, watchlist, template="ui/watchlist/list.html"):
    sorting = request.GET.get("sort", None)
    inverting = request.GET.get('inverted', False)
    if inverting == "True":
        inverting = True
    else:
        inverting = False
    if sorting:
        if sorting in ['date', 'release', 'imdb_score', 'title', 'runtime']:
            print("sort by " + sorting)
            movies = movies.order_by("{}{}".format('-' if inverting else '', sorting))
    context = {
        'watchlist': watchlist,
        'movies': movies,
        'sorting': sorting,
        'inverted': not bool(inverting)
    }
    return render(request, template_name=template, context=context)


def show_watchlist(request, watchlist_uid):
    try:
        identifier = uuid.UUID(watchlist_uid).hex
    except:
        return render(request, "ui/error.html")
    # FIXME handle this and add exception
    try:
        watchlist = Watchlist.objects.get(identifier=identifier)
    except Watchlist.DoesNotExist:
        return render(request, "ui/error.html", context={"error_message": mark_safe("This list does not exist <small><span class='fa fa-frown-o'></span></small>")})

    watchlist_movies = watchlist.watchlistmovie_set.all()

    movies = Movie.objects.filter(watchlistmovie__pk__in=watchlist_movies).order_by("title").distinct()
    return render_list(movies, request, watchlist)