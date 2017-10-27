# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class HomeViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def tearDown(self):
        pass

    def test_status_code(self):
        # should be 200
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'highLight_products.html')




"""
To know more abou the .assertSomething stuff:
https://docs.python.org/3/library/unittest.html#unittest.TestCase

And to know how the Python assert testing works in Django go to:
https://docs.djangoproject.com/en/1.11/topics/testing/tools/#assertions
"""