import uuid
from django.shortcuts import render

# Create your views here.
from movies.models import Watchlist


def show_watchlist(request, watchlist_uid):
    try:
        identifier = uuid.UUID(watchlist_uid).hex
    except:
        pass
    # FIXME handle this and add exception
    watchlist = Watchlist.objects.get(identifier=identifier)
    movies = watchlist.watchlistmovie_set
    context = {
        'watchlist': watchlist,
        'movies': movies,
    }
    return render(request, template_name="ui/watchlist/index.html", context=context)