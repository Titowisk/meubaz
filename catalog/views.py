from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Products

class HighLightView(ListView):
    # Only show the lowest price products
    template_name = "catalog/highLight_products.html"
    model = Products
    context_object_name = 'six_lowest_price'

    def get_queryset(self):
        lowest_price_products = Products.objects.order_by('price')[:6] # retorna os 6 primeiros produtos ordenados pelo preço, de forma crescente
        return lowest_price_products
   

highLight = HighLightView.as_view()

class ProductsView(ListView):

    template_name = "catalog/products_section.html"
    context_object_name = 'category_list'

    def get_queryset(self):
        # self.request acessa a requisição atual
        # self.args acessa os parâmetros não-nomeados da view
        # self.kwargs acessa os parâmetros nomeados da view
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Products.objects.filter(category=category)
        # return Products.objects.filter(category__slug=category) poderia ser assim
    
    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        # Só inserir aqui os dados desejados a serem enviados para o template
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        
        return context
        


product = ProductsView.as_view()

class ProductsDetailView(DetailView):

    template_name = 'catalog/product_detail.html'
    model = Products
    context_object_name = 'product_detail'


product_detail = ProductsDetailView.as_view()