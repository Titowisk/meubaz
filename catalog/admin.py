from django.contrib import admin

from .models import Category, Products

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']

class ProductsAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)