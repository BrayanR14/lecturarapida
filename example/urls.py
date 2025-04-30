# example/urls.py
from django.urls import path

from example.views import index, perfil, create


urlpatterns = [
    path('', index),
    path('perfil/', perfil, name='perfil'),
    path('create/', create, name='create')
]