from django.test import TestCase, Client
from django.urls import reverse
from .models import Painting
from accounts.models import Seller
from artists.models import Artist


class PaintingsTestCase(TestCase):

    def setUp(self):
        s = Seller.objects.create(email='seller@seller.com', password='dfhadfg', first_name='tom', last_name='tinko',
                              phone=4734572, description='Expensive boutique', )
        a = Artist.objects.create(name='Zinedine', nationality='French', dob='2018-10-10', dod='2019-10-10')
        Painting.objects.create(title='Mona Lisa', medium='idk', price=500, seller=s, artist=a)
        Painting.objects.create(title='Sunflowers', medium='Vangogh', price=500, seller=s, artist=a)

    def test_get_painting(self):
        response = self.client.get(reverse('paintings:get_paintings'))
        self.assertContains(response, 'medium')

    def test_delete_paintings(self):
        response = self.client.get(reverse('paintings:delete_paintings', kwargs={'id': 2}))
        self.assertEquals(response.status_code, 400)

    def tearDown(self):
        pass
