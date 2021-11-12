from django.urls import path, include

from .views import *

urlpatterns = [
    path('', mi_cv, name="MiCV"),
    path('editar/datos-personales/', datos_personales, name="datos-personales"),
    path('editar/perfil/', perfil, name="editar-perfil"),
    path('agregar/estudios', agregar_estudios, name="agregar-estudios"),
    path('editar/estudios/<int:id>/', editar_estudios, name="editar-estudios"),
    path('eliminar/estudios/<int:id>', eliminar_estudios, name="eliminar-estudios"),
    path('editar/conocimientos-y-habilidades', editar_cyh, name="editar-cyh")
]