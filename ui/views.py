import uuid
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe
from movies.models import Watchlist


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

    movies = watchlist.watchlistmovie_set.order_by("movie__title")
    sorting = request.GET.get("sort", None)
    inverting = request.GET.get('inverted', False)

    if inverting == "True":
        inverting = True
    else:
        inverting = False

    if sorting:
        if sorting in ['date', 'release', 'imdb_score', 'title', 'runtime']:
            print("sort by "+ sorting)
            movies = movies.order_by("{}movie__{}".format('-' if inverting else '', sorting))

    context = {
        'watchlist': watchlist,
        'movies': movies,
        'sorting': sorting,
        'inverted': not bool(inverting)
    }
    return render(request, template_name="ui/watchlist/list.html", context=context)