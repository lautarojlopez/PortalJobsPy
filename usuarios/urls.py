from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('registro/', registro, name="Registro"),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('mis-postulaciones/', mis_postulaciones, name="mis-postulaciones"),
    path('restablecer-contraseña/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('restablecer-contraseña/sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('restablecer-contraseña/complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]