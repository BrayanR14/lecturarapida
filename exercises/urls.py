from django.urls import path
from exercises.views import index, ejercicio


urlpatterns = [
    path('', ejercicio, name='ejercicio'),
]