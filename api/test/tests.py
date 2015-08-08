from pprint import pprint
from django.test import TestCase
from api.service import OMDBApiService
from api.test import mocks
from .. import models

class TestApi(TestCase):
    def test_import_from_api(self):
        OMDBApiService._request_api = mocks.OMDBMock._request_api_success
        OMDBApiService.import_movie("Frozen", "")

        frozen_movie = models.Movie.objects.get(title="Frozen")

        pprint(frozen_movie.__dict__)
        self.assertIsNotNone(frozen_movie)
