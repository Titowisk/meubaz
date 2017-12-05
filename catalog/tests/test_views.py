from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from catalog.models import Category, Products

class ProductsSectionTestCase(TestCase):
    # a url é recebe um parâmetro nomeado, e agora?
    def setUp(self):
        self.category = mommy.make('catalog.Category', name='livros', slug='livros')
        self.products = mommy.make('catalog.Products', _quantity=10)
        for p in self.products:
            p.category = self.category
            p.save()
        self.url = reverse('catalog:products', kwargs={'slug': self.category.slug})
        self.client = Client()

    def tearDown(self):
        for p in self.products:
            p.delete()
    
    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/products_section.html')
    
    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('category_list' in response.context)
        category_list = response.context['category_list']
        self.assertEquals(category_list.count(), 3) # cada página terá 3 produtos
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4) # deverão haver 4 páginas
        last_page_objects = paginator.page(4).object_list # a última página só terá 1 produto.
        self.assertEquals(last_page_objects.count(), 1)
    
    def test_page_not_found(self):
        response = self.client.get('{0}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404 # ao acessar uma página que não existe a saída é 404)
        

class HighLightTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('catalog:highLight')
        self.products = mommy.make('catalog.Products', _quantity=10)       

    def tearDown(self):
        Products.objects.all().delete()

    def test_status_code(self):
        # should be 200
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'catalog/highLight_products.html')

    def test_product_list(self):
        response = self.client.get(self.url)
        self.assertTrue('six_lowest_price' in response.context)
        products = response.context['six_lowest_price']
        self.assertEquals(products.count(), 6)
        # The product with the lowest price must be in the six_lowest_price products.
        lowest_price = min(Products.objects.all(), key=lambda x: x.price)
        self.assertTrue(lowest_price in products)
        
        

class ProductDetailTestCase(TestCase):
    # Fazer quando finalizar o frontend da view
    pass