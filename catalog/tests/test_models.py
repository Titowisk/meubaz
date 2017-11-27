# coding=utf-8

from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy

from catalog.models import Category, Products

class CategoryTestCase(TestCase):
    
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    def tearDown(self):
        Category.objects.all().delete()

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:products', kwargs={'slug': self.category.slug})
        )

class ProductsTestCase(TestCase):

    def setUp(self):
        self.products = mommy.make('catalog.Products')

    def tearDown(self):
        Products.objects.all().delete()

    def test_product_detail_url(self):
        self.assertEquals(
            self.products.product_detail_url(),
            reverse('catalog:product_detail', kwargs={'slug': self.products.slug})
            )