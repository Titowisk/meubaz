# coding=utf-8

from .models import Category, Products

def categories(request):
    return {'categories': Category.objects.all()}

def latest_products(request):
    latest_products = Products.objects.order_by('created').reverse()[:3]
    return {'latest_products': latest_products}
# Problema aqui Seção 2, Aula 20
