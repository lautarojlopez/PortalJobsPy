from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('registro/', registro, name="Registro"),
    path('iniciar-sesion/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('cerrar-sesion/', LogoutView.as_view(), name="logout"),
]