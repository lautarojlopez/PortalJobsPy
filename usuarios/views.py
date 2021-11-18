import django
from django.shortcuts import redirect, render
from django.contrib import messages

from CV.models import CV
from .forms import FormTipo, FormularioDatos
from usuarios.models import UserProfile

# Create your views here.

# Registro de usuarios
def registro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('Home')
        else:
            return render(request, 'registro.html')
    else:
        form_datos = FormularioDatos(request.POST)
        form_tipo = FormTipo(request.POST)

        if form_datos.is_valid() and form_tipo.is_valid():
            datos = form_datos.save()
            usuario = form_tipo.save(commit=False)
            usuario.datos = datos

            # Si es una cuenta de tipo "Postulante" crea un CV
            if form_tipo.cleaned_data['tipo_cuenta'] == "Postulante":
                cv = CV.objects.create()
                cv.nombre = f"{form_datos.cleaned_data['first_name']} {form_datos.cleaned_data['last_name']}"
                cv.email = form_datos.cleaned_data['email']
                cv.save()
                usuario.cv_id = cv.id
                
            usuario.save()
            messages.success(request, "Tu cuenta ha sido creada.")
            return redirect('login')
        else:
            return render(request, 'registro.html', {"errors": form_datos.errors})

        return render(request, 'registro.html')


def mis_postulaciones(request):
    # Busca las postulaciones del usuario en la base de datos
    usuario = UserProfile.objects.get(id=request.userprofile.datos.id)
    postulaciones = usuario.postulaciones.all()
    return render(request, 'mis-postulaciones.html', {"postulaciones": postulaciones})