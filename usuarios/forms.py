from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

# Formulario con los datos de la cuenta de usuario
class FormularioDatos(UserCreationForm):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

# Formulario para el tipo de cuenta (Empresa o Postulante)
class FormTipo(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('tipo_cuenta',)