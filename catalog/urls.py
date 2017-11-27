from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)/$', views.product, name='products'),
    url(r'^detalhes/(?P<slug>[\w_-]+)/$', views.product_detail, name='product_detail'),
]

# próximo desafio detalhes/(?P<slug>[\w_-]+)