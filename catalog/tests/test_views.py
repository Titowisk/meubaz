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
        self.assertEquals(category_list.count(), 10)




# próximo desafio: testar views que recebem parâmetros nomeados em suas urls.