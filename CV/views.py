from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render

from CV.models import CV
from .forms import FormDatosPersonales

# Create your views here.
def mi_cv(request):
    return render(request, 'mi-cv.html')

def datos_personales(request):
    if request.method == "GET":
        return render(request, 'datos-personales.html')
    elif request.method == "POST":
        form_datos_personales = FormDatosPersonales(request.POST)
        if form_datos_personales.is_valid():
            # Busca el CV del usuario en la base de datos
            cv = CV.objects.get(id=request.userprofile.cv_id)

            # Reemplaza con los datos del formulario
            cv.nombre = form_datos_personales.cleaned_data['nombre']
            cv.fecha_nacimiento = form_datos_personales.cleaned_data['fecha_nacimiento']
            cv.genero = form_datos_personales.cleaned_data['genero']
            cv.DNI = form_datos_personales.cleaned_data['DNI']
            cv.nacionalidad = form_datos_personales.cleaned_data['nacionalidad']
            cv.localidad = form_datos_personales.cleaned_data['localidad']
            cv.direccion = form_datos_personales.cleaned_data['direccion']
            cv.codigo_postal = form_datos_personales.cleaned_data['codigo_postal']
            cv.telefono = form_datos_personales.cleaned_data['telefono']
            cv.email = form_datos_personales.cleaned_data['email']

            # Guarda los cambios en la base de datos
            cv.save()

            # Redirecciona con mensaje de exito
            messages.success(request, 'Tus datos han sido guardados')
            return render(request, 'mi-cv.html')
        else:
            return render(request, 'datos-personales.html', { "errors": form_datos_personales.errors })