from django.urls import path, include

from .views import *

urlpatterns = [
    path('mi-cv/', mi_cv, name="MiCV")
]