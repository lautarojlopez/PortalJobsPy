from django.urls.conf import path
from django.urls import path
from .views import *

urlpatterns = [
    path('crear/', crear_publicacion, name="crear-publicacion"),
    path('mis-publicaciones', mis_publicaciones, name="mis-publicaciones"),
    path('<url>', ver_publicacion, name="ver-publicacion"),
    path('editar/<url>', editar_publicacion, name="editar-publicacion"),
    path('eliminar/<url>', eliminar_publicacion, name="eliminar-publicacion")
]