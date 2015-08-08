from pprint import pprint
from django.test import TestCase
from api.service import OMDBApiService
from api.test import mocks
from .. import models

USE_MOCKS = True


class TestApi(TestCase):
    def setUp(self):
        self.success_imports = 0

    def test_import_from_api(self):
        self.import_from_api(movie_title="Frozen")
        if not USE_MOCKS:
            self.import_from_api(movie_title="Jurassic Park")
            self.import_from_api(movie_title="The Lost World: Jurassic Park")
            self.import_from_api(movie_title="Kill Bill: Vol. 1")
            self.import_from_api(movie_title="1408")
            self.import_from_api(movie_title="Cloud Atlas")
            self.import_from_api(movie_title="King Kong")
        self.assertEqual(self.success_imports, models.Movie.objects.count())

    def import_from_api(self, movie_title="Frozen"):
        self.success_imports += 1
        if USE_MOCKS:
            OMDBApiService._request_api = mocks.OMDBMock._request_api_success
        OMDBApiService.import_movie(movie_title, "")

        movie = models.Movie.objects.get(title=movie_title)

        pprint(movie.__dict__)
        pprint(movie.genre.all())
        pprint(movie.actors.all())
        pprint(movie.director.all())
        self.assertIsNotNone(movie)


class TestApiError(TestCase):
    def test_import_error(self):
        if USE_MOCKS:
            OMDBApiService._request_api = mocks.OMDBMock._request_api_error
        OMDBApiService.import_movie("no_real_movie", "")
        self.assertEqual(0, models.Movie.objects.count())