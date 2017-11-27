# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catalog.models import Products

class HomeView(ListView):

    template_name = "highLight_products.html"
    model = Products
    context_object_name = 'products'

    
class ContactView(TemplateView):

    template_name = "contact_section.html"


home = HomeView.as_view()
contact = ContactView.as_view()

"""
def home(request):
    template = 'highLight_products.html'
    return render(request, template)

def contact(request):
    template = 'contact_section.html'
    return render(request, template)

"""