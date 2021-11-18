from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('registro/', registro, name="Registro"),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('mis-postulaciones/', mis_postulaciones, name="mis-postulaciones")
]