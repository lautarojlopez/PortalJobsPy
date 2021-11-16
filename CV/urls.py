from os import name
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    # Ver CV
    path('', mi_cv, name="MiCV"),
    # Edicion de datos personales
    path('editar/datos-personales/', editar_datos_personales, name="datos-personales"),
    # Edicion de perfil
    path('editar/perfil/', editar_perfil, name="editar-perfil"),
    # Agregar, editar y eliminar estudios
    path('agregar/estudios', agregar_estudios, name="agregar-estudios"),
    path('editar/estudios/<int:id>/', editar_estudios, name="editar-estudios"),
    path('eliminar/estudios/<int:id>', eliminar_estudios, name="eliminar-estudios"),
    # Edicion de conocimientos y habilidades
    path('editar/conocimientos-y-habilidades', editar_cyh, name="editar-cyh"),
    # Agregar, editar y eliminar experiencias laborales
    path('agregar/experiencia', agregar_experiencia, name="agregar-experiencia"),
    path('eliminar/experiencia/<int:id>', eliminar_experiencia, name="eliminar-experiencia"),
    path('editar/experiencia/<int:id>', editar_experiencia, name='editar-experiencia'),
    # Editar datos adicionales
    path('editar/otros', editar_otros, name="editar-otros"),
    # Agregar, editar y eliminar idiomas
    path('agregar/idioma', agregar_idioma, name="agregar-idioma"),
    path('eliminar/idioma/<int:id>', eliminar_idioma, name="eliminar-idioma"),
    path('editar/idioma/<int:id>', editar_idioma, name="editar-idioma")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)