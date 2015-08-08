from django.http import HttpResponse
from django.shortcuts import render
from api.service import OMDBApiService as api


def import_movie(request):
    movie = api.get_or_import_movie(request.GET.get("movie_title"))
    if movie:
        return HttpResponse(movie.__str__())
    else:
        return HttpResponse("Not found! :(")