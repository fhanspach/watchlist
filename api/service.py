from . import models
from pprint import pprint
import arrow
from decimal import Decimal
from parse import parse
import requests


class OMDBApiService(object):
    API_URL = "http://www.omdbapi.com/?t={title}&y={year}&plot=full&r=json"

    @staticmethod
    def _get_release_date(api_response):
        return arrow.get(api_response.get("Released"), 'DD MMM YYYY').date()

    @staticmethod
    def import_movie(movie_title, year=None):
        api_response = OMDBApiService._request_api(movie_title=movie_title, year=year)

        movie = models.Movie(title=api_response.get("Title"),
                             rating=api_response.get("Rated"),
                             runtime=int(parse("{:d} min", api_response.get("Runtime", "0 min"))[0]),
                             writer=api_response.get("Writer"),
                             plot=api_response.get("Plot"),
                             country=api_response.get("Country"),
                             poster=api_response.get("Poster"),
                             imdb_score=Decimal(api_response.get("imdbRating")),
                             release=OMDBApiService._get_release_date(api_response)
                             )
        movie.save()
        return movie

    @staticmethod
    def _request_api(movie_title, year):
        print("Api call for {}".format(movie_title))
        response = requests.get(OMDBApiService.API_URL.format(title=movie_title, year=year or ""))
        pprint(response.json())
        if not response.status_code == requests.codes.ok:
            response.raise_for_status()
        return response.json()

    @staticmethod
    def _add_generes(movie: "Movie", genere_string:str):
        genere_names = genere_string.split(",")
        for name in genere_names:
            genere = models.Genre.objects.get_or_create(title=name)
            movie.genre.add(genere)
        movie.save()

    @staticmethod
    def _add_persons(movie: "Movie", persons_string:str, role:str):
        if role != "director" and role != "actor":
            raise ValueError("role must be 'director' or 'actor")

        person_names = persons_string.split(",")
        for name in person_names:
            person = models.Person.objects.get_or_create(title=name)
            if role == "director":
                movie.director.add(person)
            elif role == "actor":
                movie.actors.add(person)

        movie.save()