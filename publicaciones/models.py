from django.db import models
from usuarios.models import UserProfile

# Create your models here.
class Publicacion(models.Model):  
    puesto = models.CharField(max_length=150)
    descripcion = models.TextField()
    area = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50)
    sueldo = models.IntegerField()
    tipo = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    autor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    postulantes = models.ManyToManyField(UserProfile, related_name="postulaciones")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)