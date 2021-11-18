from django.shortcuts import redirect, render
from django.http import JsonResponse
from .froms import FormPublicacion
from .models import Publicacion
from django.utils.text import slugify
import shortuuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

# Muestra las publicaciones de ofertas de trabajo creadas por el usuario
@login_required
def mis_publicaciones(request):
    publicaciones = Publicacion.objects.filter(autor_id=request.userprofile.id).order_by('-created_at')
    return render(request, 'mis-publicaciones.html', {"publicaciones": publicaciones})

# Crear una publicación
@login_required
def crear_publicacion(request):
    if request.method == "GET":
        return render(request, 'crear-publicacion.html')
    if request.method == "POST":
        form_publicacion = FormPublicacion(request.POST)
        if form_publicacion.is_valid():
            try:
                datos = form_publicacion.cleaned_data
                slug = f"{slugify( datos['puesto'] )}-{shortuuid.uuid()}"
                datos['url'] = slug
                datos['autor_id'] = request.userprofile.id
                nueva_publicacion = Publicacion.objects.create(
                    puesto = datos['puesto'],
                    descripcion = datos['descripcion'],
                    sueldo = datos['sueldo'],
                    area = datos['area'],
                    localidad = datos['localidad'],
                    tipo = datos['tipo'],
                    modalidad = datos['modalidad'],
                    url = datos['url'],
                    autor_id = datos['autor_id']
                )
                nueva_publicacion.save()
                messages.success(request, 'Publicación creada correctamente')
                return redirect("mis-publicaciones")
            except:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("mis-publicaciones")

        else:
            return render(request, 'crear-publicacion.html', {"errors": form_publicacion.errors})

# Muestra una publicación
def ver_publicacion(request, url):
    publicacion = Publicacion.objects.get(url=url)
    return render(request, 'ver-publicacion.html', {"publicacion": publicacion})

# Editar una publicación
@login_required
def editar_publicacion(request, url):
    # Busca la publicacion a editar en la base de datos
    publicacion = Publicacion.objects.get(url=url)

    # Si el usuario no es el creador de la publicación, redirecciona a 403
    if not publicacion.autor_id == request.userprofile.id:
        return redirect('403')

    if request.method == "GET":
        return render(request, 'editar-publicacion.html', {"publicacion": publicacion})
    if request.method == "POST":
        form_publicacion = FormPublicacion(request.POST)
        if form_publicacion.is_valid():
            try:
                datos = form_publicacion.cleaned_data
                publicacion.puesto = datos['puesto']
                publicacion.descripcion = datos['descripcion']
                publicacion.sueldo = datos['sueldo']
                publicacion.area = datos['area']
                publicacion.localidad = datos['localidad']
                publicacion.tipo = datos['tipo']
                publicacion.modalidad = datos['modalidad']
                publicacion.save()
                messages.success(request, 'Publicación editada correctamente')
                return redirect("mis-publicaciones")
            except Exception as e:
                # Redirecciona con mensaje de error
                messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
                return redirect("mis-publicaciones")
        else:
            return render(request, 'editar-publicacion.html', {"publicacion": publicacion, "errors": form_publicacion.errors})

# Eliminar una publicación
@login_required
def eliminar_publicacion(request, url):
    # Busca la publicacion a editar en la base de datos
    publicacion = Publicacion.objects.get(url=url)

    # Si el usuario no es el creador de la publicación, redirecciona a 403
    if not publicacion.autor_id == request.userprofile.id:
        return redirect('403')

    if request.method == "GET":
        return render(request, 'eliminar-publicacion.html', {"publicacion": publicacion})
    if request.method == "POST":
        try:
            publicacion.delete()
            messages.success(request, 'Publicación eliminada correctamente')
            return redirect("mis-publicaciones")
        except Exception as e:
            # Redirecciona con mensaje de error
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect("mis-publicaciones")

# Postular a una oferta
@login_required
def postular(request, url):
    # Busca la publicacion a editar en la base de datos
    publicacion = Publicacion.objects.get(url=url)
    if request.userprofile.tipo_cuenta == "Postulante":
        try:
            publicacion.postulantes.add(request.userprofile)
            return redirect(f'/publicaciones/{url}')
        except:
            messages.error(request, 'Ups... Algo ha salido mal. Vuelve a intentarlo.')
            return redirect(f'/publicaciones/{url}')
    else:
        return redirect('403')

# Ver postulantes a una oferta de trabajo
@login_required
def ver_postulantes(request, url):
    # Busca la publicacion a editar en la base de datos
    publicacion = Publicacion.objects.get(url=url)

    # Si el usuario no es el creador de la publicación, redirecciona a 403
    if not publicacion.autor_id == request.userprofile.id:
        return redirect('403')
    else:
        postulantes = publicacion.postulantes.all()
        return render(request, 'ver-postulantes.html', {"publicacion": publicacion, "postulantes": postulantes})

# Ver CV de un postulante
@login_required
def cv_postulante(request, url, id):
    # Busca la publicacion a editar en la base de datos
    publicacion = Publicacion.objects.get(url=url)

    # Si el usuario no es el creador de la publicación, redirecciona a 403
    if not publicacion.autor_id == request.userprofile.id:
        return redirect('403')
    else:
        cv_postulante = publicacion.postulantes.all()[id].cv
        return render(request, 'ver-cv-postulante.html', {"cv": cv_postulante})