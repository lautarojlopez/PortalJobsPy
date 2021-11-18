from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from publicaciones.models import Publicacion
from usuarios.models import UserProfile

# Create your views here.
def home(request):
    publicaciones = Publicacion.objects.all()[:9]
    return render(request, 'index.html', {"publicaciones": publicaciones})

def error_403(request):
    return render(request, '403.html')

def mis_postulaciones(request):
    # Busca las postulaciones del usuario en la base de datos
    usuario = UserProfile.objects.get(id=request.userprofile.datos.id)
    postulaciones = usuario.postulaciones.all()
    return render(request, 'mis-postulaciones.html', {"postulaciones": postulaciones})