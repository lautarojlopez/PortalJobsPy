from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from CV.models import CV
from PortalJobs.settings import BASE_DIR
from .forms import FormDatosPersonales, FormEstudios, FormExperiencia
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
@login_required
def mi_cv(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')

    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)

    return render(request, 'mi-cv.html', { "cv": cv })

# Edicion de datos personales
@login_required
def editar_datos_personales(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')

    if request.method == "GET":
        # Busca el cv en la base de datos
        cv = CV.objects.get(id=request.userprofile.cv_id)
        return render(request, 'datos-personales.html', { "cv": cv })

    elif request.method == "POST":
        
        form_datos_personales = FormDatosPersonales(request.POST, request.FILES)

        if form_datos_personales.is_valid():
            datos = form_datos_personales.cleaned_data
            print(datos)
            # Busca el CV del usuario en la base de datos
            cv = CV.objects.get(id=request.userprofile.cv_id)
            try:
                # Reemplaza con los datos del formulario
                cv.nombre = datos['nombre']
                cv.fecha_nacimiento = datos['fecha_nacimiento']
                cv.genero = datos['genero']
                cv.DNI = datos['DNI']
                cv.nacionalidad = datos['nacionalidad']
                cv.localidad = datos['localidad']
                cv.direccion = datos['direccion']
                cv.codigo_postal = datos['codigo_postal']
                cv.telefono = datos['telefono']
                cv.email = datos['email']
                if datos['imagen'] is not None:
                    cv.imagen = datos['imagen']

                cv.completo = True
                # Guarda los cambios en la base de datos
                cv.save()

                # Redirecciona con mensaje de exito
                messages.success(request, 'Tus datos han sido guardados')
                return redirect("MiCV")

            except Exception as e:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("MiCV")

        else:

            return render(request, 'datos-personales.html', { "errors": form_datos_personales.errors })

# Edicion de perfil
@login_required
def editar_perfil(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')

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
@login_required
def agregar_estudios(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')

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
@login_required
def editar_estudios(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
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
@login_required
def eliminar_estudios(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        

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
@login_required
def editar_cyh(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
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
@login_required
def agregar_experiencia(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
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

# Eliminar una experiencia laboral del arreglo de experiencias
@login_required
def eliminar_experiencia(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
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
@login_required
def editar_experiencia(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')

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

# Editar datos adicionales
@login_required
def editar_otros(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    if request.method == "GET":
        return render(request, 'editar-otros.html', {"cv": cv})
    if request.method == "POST":
        try:
            licencias = request.POST.getlist('licencia')
            cv.licencias = licencias
            cv.movilidad_propia = bool(int(request.POST['movilidad_propia']))
            cv.disponibilidad_viajar = bool(int(request.POST['disponibilidad_viajar']))
            cv.disponibilidad_mudarse = bool(int(request.POST['disponibilidad_mudarse']))
            cv.save()
            messages.success(request, 'Datos editados correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

# Agrega un idioma al arreglo de idiomas
@login_required
def agregar_idioma(request):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    idiomas = cv.idiomas

    if request.method == "GET":
        return render(request, 'agregar-idioma.html')
    if request.method == "POST":
        try:
            # ID para luego poder editar o eliminar el idioma del arreglo
            if len(cv.idiomas) == 0:
                # Si el arreglo está vacío el ID será 0
                id = 0
            else:
                # Sino, toma el id del ultimo elemento del arreglo y le suma 1
                id = int(cv.idiomas[-1]['id']) + 1
            idioma = {
                "id": id,
                "idioma": request.POST['idioma'],
                "nivel": request.POST['nivel'],
            }
            idiomas.append(idioma)
            cv.save()
            messages.success(request, 'Idioma agregado correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

# Eliminar un idioma del arreglo de idiomas
@login_required
def eliminar_idioma(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        

    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca el idioma a eliminar en el arreglo de idiomas
    for _idioma in cv.idiomas:
        if int(_idioma['id']) == id:
            idioma = _idioma

    if request.method == "GET":
        return render(request, 'eliminar-idioma.html', { "idioma": idioma })
    if request.method == "POST":
        try:
            cv.idiomas.remove(idioma)
            cv.save()
            messages.success(request, 'Idioma eliminado correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")

# Editar un idioma del arreglo de idiomas
@login_required
def editar_idioma(request, id):
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('403')
        
    # Si no es una cuenta de tipo postulante, redirecciona al inicio
    if not request.userprofile.tipo_cuenta == "Postulante":
        return redirect('Home')
    # Busca el CV del usuario en la base de datos
    cv = CV.objects.get(id=request.userprofile.cv_id)
    # Busca el idioma a eliminar en el arreglo de idiomas
    for _idioma in cv.idiomas:
        if int(_idioma['id']) == id:
            idioma = _idioma

    if request.method == "GET":
        return render(request, 'editar-idioma.html', { "idioma": idioma })
    if request.method == "POST":
        try:
            idioma['idioma'] = request.POST['idioma']
            idioma['nivel'] = request.POST['nivel']
            cv.save()
            messages.success(request, 'Idioma editado correctamente')
            return redirect("MiCV")
        except:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("MiCV")
