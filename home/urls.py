from django.urls import path

from home.views import index, perfil, create


urlpatterns = [
    path('', index),
    path('perfil/', perfil, name='perfil'),
    path('create/', create, name='create')
]