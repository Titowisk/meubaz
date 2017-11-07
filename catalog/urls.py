from django.conf.urls import url
from .views import ProductsView

urlpatterns = [
    url(r'^produtos/$', ProductsView.as_view(), name='products'),
]