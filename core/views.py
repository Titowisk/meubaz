# coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Alguma coisa"""

    template_name = "base.html"


