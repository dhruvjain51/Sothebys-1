from django.test import TestCase, Client
from django.urls import reverse
from .models import Buyer, Seller


class AccountsTestCase(TestCase):

    def setUp(self):
        Buyer.objects.create(email='buyer@buyer.com', password='abcd', first_name='bob', last_name='miller',
                             phone=123456, shipping='Charlotte, NC')
        Seller.objects.create(email='seller@seller.com', password = 'dfhadfg', first_name='tom', last_name='tinko',
                              phone=4734572, description='Expensive boutique',)

    def test_get_buyers(self):
        response = self.client.get(reverse('accounts:get_buyers'))
        buyer = Buyer.objects.get(first_name='bob')
        self.assertContains(response, 'first_name')

    def test_get_sellers(self):
        response = self.client.get(reverse('accounts:get_sellers'))
        self.assertContains(response, 'description')

    def tearDown(self):
        pass


