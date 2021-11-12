from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from CV.models import CV
from .forms import FormDatosPersonales, FormEstudios

# Create your views here.
def mi_cv(request):

    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)

    return render(request, 'mi-cv.html', { "cv": cv })

# Edicion de datos personales
def datos_personales(request):
    if request.method == "GET":
        # Busca el cv en la base de datos
        cv = CV.objects.get(id=request.userprofile.cv_id)
        return render(request, 'datos-personales.html', { "cv": cv })

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
            return redirect("MiCV")

        else:

            return render(request, 'datos-personales.html', { "errors": form_datos_personales.errors })

# Edicion de perfil
def perfil(request):
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)

    if request.method == "GET":

        return render(request, 'perfil.html', { "cv": cv })

    elif request.method == "POST":
        
        try:
            cv.perfil = request.POST['perfil']
            cv.save()
            # Redirecciona con mensaje de exito
            messages.success(request, 'Tus datos han sido guardados')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

def agregar_estudios(request):
    if request.method == "GET":
        return render(request, 'agregar-estudios.html')
    elif request.method == "POST":
        # Busca el CV del usuario en la base de datos
        cv = CV.objects.get(id=request.userprofile.cv_id)
        
        # Validar los datos con formulario
        form_estudios = FormEstudios(request.POST)

        # Si es valido, agrega los datos
        if form_estudios.is_valid():
            try:
                estudios = form_estudios.cleaned_data
                if cv.estudios is None or cv.estudios == []:
                    cv.estudios = [{
                        "id": 1,
                        "titulo": estudios['titulo'],
                        "institucion": estudios['institucion'],
                        "tipo": estudios['tipo'],
                        "estado": estudios['estado'],
                        "mes_desde": estudios['mes_desde'],
                        "anio_desde": estudios['anio_desde'],
                        "mes_hasta": estudios['mes_hasta'],
                        "anio_hasta": estudios['anio_hasta']
                    }]
                else:
                    print(cv.estudios[-1]['id'])
                    cv.estudios.append({
                        "id": int(cv.estudios[-1]['id']) + 1,
                        "titulo": estudios['titulo'],
                        "institucion": estudios['institucion'],
                        "tipo": estudios['tipo'],
                        "estado": estudios['estado'],
                        "mes_desde": estudios['mes_desde'],
                        "anio_desde": estudios['anio_desde'],
                        "mes_hasta": estudios['mes_hasta'],
                        "anio_hasta": estudios['anio_hasta']
                    })
                cv.save()

                # Redirecciona con mensaje de exito
                messages.success(request, 'Tus datos han sido guardados')
                return redirect("MiCV")

            except:

                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("MiCV")
        # Si no es valido, redirige con errores
        else:
            return render(request, 'agregar-estudios.html', { "errors": form_estudios.errors })

def editar_estudios(request, id):
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca el objeto a editar en el arreglo de estudios
    estudios = cv.estudios[id-1]
    
    if request.method == "GET":

        return render(request, 'editar-estudios.html', { "estudio": estudios })

    elif request.method == "POST":

        # Validar los datos con formulario
        form_estudios = FormEstudios(request.POST)

        # Si es valido, reemplaza los datos
        if form_estudios.is_valid():
            try:
                datos = form_estudios.cleaned_data
                estudios['titulo'] = datos['titulo']
                estudios['institucion'] = datos['institucion']
                estudios['tipo'] = datos['tipo']
                estudios['estado'] = datos['estado']
                estudios['mes_desde'] = datos['mes_desde']
                estudios['anio_desde'] = datos['anio_desde']
                estudios['mes_hasta'] = datos['mes_hasta']
                estudios['anio_hasta'] = datos['anio_hasta']
                cv.save()
                 # Redirecciona con mensaje de exito
                messages.success(request, 'Tus datos han sido guardados')
                return redirect("MiCV")
            except:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("MiCV")
        # Si no es valido, redirige con errores
        else:
            print(form_estudios.cleaned_data)
            return render(request, 'editar-estudios.html', { "errors": form_estudios.errors, "estudio": estudios })

def eliminar_estudios(request, id):

    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca el objeto a editar en el arreglo de estudios
    estudios = cv.estudios[id-1]

    if request.method == "GET":
        return render(request, 'eliminar-estudios.html', {"estudios": estudios})
    if request.method == "POST":
        try:
            cv.estudios.remove(estudios)
            cv.save()
            # Redirecciona con mensaje de éxito
            messages.success(request, 'Estudios eliminados correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")