from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Products


class ProductsView(ListView):

    template_name = "catalog/products_section.html"
    model = Products


