from django.test import TestCase, Client
from django.urls import reverse
import datetime
from .models import Artist


class ArtistsTestCase(TestCase):

    def setUp(self):
        Artist.objects.create(name='Zinedine', nationality='French', dob='2018-10-10', dod='2019-10-10')

    def test_get_artists(self):
        response = self.client.get(reverse('artists:get_artists'))
        self.assertContains(response, 'nationality')

    def tearDown(self):
        pass


