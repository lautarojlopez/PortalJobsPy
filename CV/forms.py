from django import forms
from .models import CV

class FormDatosPersonales(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('nombre', 'fecha_nacimiento', 'genero', 'DNI', 'nacionalidad', 'localidad', 'direccion', 'codigo_postal', 'telefono', 'email')