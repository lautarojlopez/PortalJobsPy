from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from CV.models import CV
from .forms import FormDatosPersonales, FormEstudios, FormExperiencia

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

# Agregar estudios al arreglo de estudios en CV
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

# Editar un estudio
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
            return render(request, 'editar-estudios.html', { "errors": form_estudios.errors, "estudio": estudios })

# Eliminar estudios del arreglo de estudios en CV
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

# Edicion de Conocimientos y Habilidades
def editar_cyh(request):
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    if request.method == "GET":
        return render(request, 'editar-cyh.html', {"cv": cv})
    if request.method == "POST":
        try:
            cv.habilidades = request.POST['habilidades']
            cv.save()
            # Redirecciona con mensaje de éxito
            messages.success(request, 'Estudios eliminados correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

# Agregar experiencia al arreglo experiencias en CV
def agregar_experiencia(request):
    if request.method == "GET":
        return render(request, 'agregar-experiencia.html')
    if request.method == "POST":
        # Busca el CV del usuario en la base de datos
        cv = CV.objects.get(id=request.userprofile.cv_id)
        form_experiencia = FormExperiencia(request.POST)

        if form_experiencia.is_valid():
            try:
                datos = form_experiencia.cleaned_data
                # ID para luego poder borrar o editar la experiencia
                if len(cv.experiencia) == 0:
                    # Si el arreglo está vacío, el id será cero
                    id = 0
                else:
                    # Sino, toma el id del ultimo elemento del arreglo y le suma 1
                    id = int(cv.experiencia[-1]['id']) + 1
                experiencia = {
                    "id": id,
                    "puesto": datos['puesto'],
                    "empresa": datos['empresa'],
                    "descripcion": datos['descripcion'],
                    "mes_desde": datos['mes_desde'],
                    "anio_desde": datos['anio_desde'],
                    "mes_hasta": datos['mes_hasta'],
                    "anio_hasta": datos['anio_hasta']
                }
                cv.experiencia.append(experiencia)
                cv.save()
                # Redirecciona con mensaje de éxito
                messages.success(request, 'Experiencia agregada correctamente')
                return redirect("MiCV")
            except:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("MiCV")
        else:
            return render(request, 'agregar-experiencia.html', { "errors": form_experiencia.errors })

def eliminar_experiencia(request, id):
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca la experiencia a eliminar en el arreglo de experiencias
    experiencia = cv.experiencia[id-1]
    if request.method == "GET":
        return render(request, 'eliminar-experiencia.html', {"experiencia": experiencia})
    if request.method == "POST":
        try:
            cv.experiencia.remove(experiencia)
            cv.save()
             # Redirecciona con mensaje de éxito
            messages.success(request, 'Experiencia eliminada correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

# Editar una experiencia laboral
def editar_experiencia(request, id):

    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca la experiencia a editar en el arreglo de experiencias
    experiencia = cv.experiencia[id]

    if request.method == "GET":
        return render(request, 'editar-experiencia.html', {"experiencia": experiencia})
    if request.method == "POST":
        form_experiencia = FormExperiencia(request.POST)
        if form_experiencia.is_valid():
            datos = form_experiencia.cleaned_data
            try:
                experiencia['puesto'] = datos['puesto']
                experiencia['empresa'] = datos['empresa']
                experiencia['descripcion'] = datos['descripcion']
                experiencia['mes_desde'] = datos['mes_desde']
                experiencia['anio_desde'] = datos['anio_desde']
                experiencia['mes_hasta'] = datos['mes_hasta']
                experiencia['anio_hasta'] = datos['anio_hasta']

                cv.save()
                messages.success(request, 'Experiencia editada correctamente')
                return redirect("MiCV")
            except:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("MiCV")
        else:
            return render(request, 'editar-experiencia.html', { "errors": form_experiencia.errors, "experiencia": experiencia })