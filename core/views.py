# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catalog.models import Products

class IndexView(TemplateView):

    template_name = "index.html"

    
class ContactView(TemplateView):

    template_name = "contact_section.html"

index = IndexView.as_view()
contact = ContactView.as_view()

"""
def home(request):
    template = 'highLight_products.html'
    return render(request, template)

def contact(request):
    template = 'contact_section.html'
    return render(request, template)

"""