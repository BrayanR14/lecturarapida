# example/urls.py
from django.urls import path

from example.views import index, perfil


urlpatterns = [
    path('', index),
    path('perfil/', perfil),
]