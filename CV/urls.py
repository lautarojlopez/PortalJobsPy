from django.urls import path, include

from .views import *

urlpatterns = [
    path('', mi_cv, name="MiCV"),
    path('editar/datos-personales/', datos_personales, name="datos-personales")
]