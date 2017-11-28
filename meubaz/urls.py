
from django.conf.urls import url, include
from django.contrib import admin

from core import views

urlpatterns = [
    url(r'^categoria/', include('catalog.urls', namespace='catalog') ),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^$', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
]

