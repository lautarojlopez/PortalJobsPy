from django import forms
from .models import CV
from django.core.exceptions import ValidationError
import datetime

class FormDatosPersonales(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('nombre', 'fecha_nacimiento', 'genero', 'DNI', 'nacionalidad', 'localidad', 'direccion', 'codigo_postal', 'telefono', 'email', 'imagen')
    
    def clean_imagen(self):
        imagen = self.cleaned_data['imagen']
        if imagen:
            if imagen.size > 5000000:
                raise ValidationError("El tamaño de la imagen es mayor a 5MB.")
            return imagen

# Formulario para agregar estudios
class FormEstudios(forms.Form):

    titulo = forms.CharField(max_length=150, required=True)
    institucion = forms.CharField(max_length=150, required=True)
    tipo = forms.CharField(max_length=15, required=True)
    estado = forms.CharField(max_length=15, required=True)
    mes_desde = forms.CharField(max_length=10, required=True)
    anio_desde = forms.IntegerField(required=True)
    mes_hasta = forms.CharField(max_length=10, required=True)
    anio_hasta = forms.IntegerField(required=True)

    # Valida que el año de inicio sea menor al de finalización
    def clean(self):
        cleaned_data = super().clean()
        
        mes_desde = cleaned_data['mes_desde']
        mes_hasta = cleaned_data['mes_hasta']
        anio_desde = cleaned_data['anio_desde']
        anio_hasta = cleaned_data['anio_hasta']

        meses = {
            "Enero": 1,
            "Febrero": 2,
            "Marzo": 3,
            "Abril": 4,
            "Mayo": 5,
            "Junio": 6,
            "Julio": 7,
            "Agosto": 8,
            "Septiembre": 9,
            "Octubre": 10,
            "Noviembre": 11,
            "Diciembre": 12
        }

        if mes_desde == "NULL":
            raise ValidationError('Selecciona un mes de inicio')
        if mes_hasta == "NULL":
            raise ValidationError('Selecciona un mes de finalización')
        if anio_desde == -1:
            raise ValidationError('Selecciona un año de inicio')
        if anio_hasta == -1:
            raise ValidationError('Selecciona un año de finalización')

        if anio_hasta < anio_desde:
            raise ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')
        elif anio_hasta == anio_desde:
            if meses.get(mes_hasta) < meses.get(mes_desde):
                raise ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')

# Formulario para experiencias laborales
class FormExperiencia(forms.Form):

    puesto = forms.CharField(max_length=150, required=True)
    empresa = forms.CharField(max_length=150, required=True)
    descripcion = forms.CharField()
    mes_desde = forms.CharField(max_length=10, required=True)
    anio_desde = forms.IntegerField(required=True)
    mes_hasta = forms.CharField(max_length=10, required=True)
    anio_hasta = forms.IntegerField(required=True)

    # Valida que el año de inicio sea menor al de finalización
    def clean(self):
        cleaned_data = super().clean()
        
        mes_desde = cleaned_data['mes_desde']
        mes_hasta = cleaned_data['mes_hasta']
        anio_desde = cleaned_data['anio_desde']
        anio_hasta = cleaned_data['anio_hasta']

        meses = {
            "Enero": 1,
            "Febrero": 2,
            "Marzo": 3,
            "Abril": 4,
            "Mayo": 5,
            "Junio": 6,
            "Julio": 7,
            "Agosto": 8,
            "Septiembre": 9,
            "Octubre": 10,
            "Noviembre": 11,
            "Diciembre": 12
        }

        if mes_desde == "NULL":
            raise ValidationError('Selecciona un mes de inicio')
        if mes_hasta == "NULL":
            raise ValidationError('Selecciona un mes de finalización')
        if anio_desde == -1:
            raise ValidationError('Selecciona un año de inicio')
        if anio_hasta == -1:
            raise ValidationError('Selecciona un año de finalización')

        if anio_hasta < anio_desde:
            raise ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')
        elif anio_hasta == anio_desde:
            if meses.get(mes_hasta) < meses.get(mes_desde):
                raise ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')