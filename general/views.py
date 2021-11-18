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

def buscar(request):
    # Busca en la base de datos
    busqueda = request.GET
    resultados = Publicacion.objects.filter(puesto__icontains=busqueda['puesto'], area__icontains=busqueda['area'], localidad__icontains=busqueda['localidad'])
    print(resultados)
    return render(request, 'busqueda.html', {"busqueda": busqueda, "resultados": resultados})