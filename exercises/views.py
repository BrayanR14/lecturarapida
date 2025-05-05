from django.shortcuts import render
from django.http import HttpResponse
from .models import Ejercicio, Estadoejercicio

def index(request):
    Eje = Ejercicio(nombre="Ejercicio1", descripcion="Descripcion del ejercicio 1", dificultad="Facil", categoria="Categoria1")
    Eje.save()
    
    est = Estadoejercicio(ejercicio=Eje, resultado="Resultado del ejercicio 1")
    est.save()
    
    est1 = Estadoejercicio(ejercicio=Eje, resultado="Resultado del ejercicio 1")
    est1.save()
    
    result = est1.ejercicio.nombre
    
    return HttpResponse(result)
