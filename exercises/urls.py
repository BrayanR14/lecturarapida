from django.urls import path
from exercises.views import index


urlpatterns = [
    path('', index),
]