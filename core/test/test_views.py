# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalog.models import Category, Products

class HomeViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')
        self.products = mommy.make('catalog.Products', _quantity=10)
        

    def tearDown(self):
        Products.objects.all().delete()

    def test_status_code(self):
        # should be 200
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'highLight_products.html')

    def test_product_list(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        products = response.context['products']
        self.assertEquals(products.count(), 10)
        







"""
To know more abou the .assertSomething stuff:
https://docs.python.org/3/library/unittest.html#unittest.TestCase

And to know how the Python assert testing works in Django go to:
https://docs.djangoproject.com/en/1.11/topics/testing/tools/#assertions
"""