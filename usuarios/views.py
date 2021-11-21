import django
from django import template
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from CV.models import CV
from .forms import FormTipo, FormularioDatos
from usuarios.models import UserProfile
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User

# Create your views here.

# Registro de usuarios

# Enviar email para confirmar cuenta
def mail_confirmar_cuenta(email, template, titulo, body,context):
    template = get_template(template)
    content = template.render(context)
    email = EmailMultiAlternatives(
        titulo,
        body,
        settings.EMAIL_HOST_USER,
        [email]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

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

# Ver a que ofertas se postuló el usuario
@login_required
def mis_postulaciones(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
    # Busca las postulaciones del usuario en la base de datos
    usuario = UserProfile.objects.get(id=request.userprofile.datos.id)
    postulaciones = usuario.postulaciones.all()
    return render(request, 'mis-postulaciones.html', {"postulaciones": postulaciones})

# # Restablecer contraseña
# def form_reset_password(request):
#     if request.method == "GET":
#         return render(request, 'reset-password.html')
#     if request.method == "POST":
#         if request.POST['username']:
#             usuario = User.objects.get(username=request.POST['username'])
#             print(usuario)
#             type(print(usuario.email))
#             if usuario:
#                 # Crea el token para confirmar la creación de la cuenta
#                 token_generator = PasswordResetTokenGenerator()
#                 token = token_generator.make_token(usuario)

#                 # Enviar email de confirmacion
#                 mail_confirmar_cuenta(usuario.email,
#                                     'email-reset-password.html',
#                                     'Restablecer Contraseña',
#                                     'Restablecer',
#                                     context={
#                                             "usuario": request.POST['username'],
#                                             "request": request,
#                                             "token": token,
#                                             "id": usuario.id
#                                         }
#                                     )
#             messages.success(request, "Mensaje enviado. Revisa tu casilla de correo electrónico.")
#             return redirect('login')
#         else:
#             messages.error(request, "Escribe un nombre de usuario.")
#             return redirect('reset-password')

# def reset_password(request):
#     if request.method == "GET":
#         return JsonResponse(request.GET)