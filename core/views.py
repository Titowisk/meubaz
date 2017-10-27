# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Alguma coisa"""

    template_name = "highLight_products.html"

class ProductsView(TemplateView):

    template_name = "products_section.html"

class ContactView(TemplateView):

    template_name = "contact_section.html"


