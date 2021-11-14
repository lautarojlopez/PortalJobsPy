from os import name
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', mi_cv, name="MiCV"),
    path('editar/datos-personales/', editar_datos_personales, name="datos-personales"),
    path('editar/perfil/', editar_perfil, name="editar-perfil"),
    path('agregar/estudios', agregar_estudios, name="agregar-estudios"),
    path('editar/estudios/<int:id>/', editar_estudios, name="editar-estudios"),
    path('eliminar/estudios/<int:id>', eliminar_estudios, name="eliminar-estudios"),
    path('editar/conocimientos-y-habilidades', editar_cyh, name="editar-cyh"),
    path('agregar/experiencia', agregar_experiencia, name="agregar-experiencia"),
    path('eliminar/experiencia/<int:id>', eliminar_experiencia, name="eliminar-experiencia"),
    path('editar/experiencia/<int:id>', editar_experiencia, name='editar-experiencia'),
    path('editar/otros', editar_otros, name="editar-otros"),
    path('agregar/idioma', agregar_idioma, name="agregar-idioma")
]