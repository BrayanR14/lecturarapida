from django.db import models

class Usuario(models.Model):
    User = models.CharField(max_length=100)
    Puntos = models.IntegerField()
    Nivel = models.IntegerField()
    Objetivos = models.CharField(max_length=100)
    Amistades = models.TextField()

    def __str__(self):
        return self.Usuario
    
class Nivel(models.Model):
    Nombre_nivel = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Puntos_Necesarios = models.IntegerField()
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='nivel_usuario')
    def __str__(self):
        return self.usuario.User 