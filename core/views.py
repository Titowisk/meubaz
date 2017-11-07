# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Alguma coisa"""

    template_name = "highLight_products.html"
    
class ContactView(TemplateView):

    template_name = "contact_section.html"


home = HomeView.as_view()
contact = ContactView.as_view()