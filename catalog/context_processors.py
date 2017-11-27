# coding=utf-8

from .models import Category

def categories(request):
    return {'categories': Category.objects.all()}

# Problema aqui Seção 2, Aula 20
