from django.db import models, migrations
from django.contrib.postgres.operations import HStoreExtension
from django.contrib.postgres.fields import HStoreField, ArrayField
from django.contrib.postgres.operations import HStoreExtension, UnaccentExtension

# Habilita el uso de HStoreField
class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        HStoreExtension(),
        UnaccentExtension()
    ]

# Función para setear por defecto las licencias de conducir
def licencia_default():
    return(list(["No Posee"]))

# Create your models here.
class CV(models.Model):

    nombre = models.CharField(max_length=50, null=True, blank=True)
    DNI = models.BigIntegerField(null=True, blank=True)
    fecha_nacimiento = models.CharField(max_length=15, null=True, blank=True)
    genero = models.CharField(max_length=15, null=True, blank=True)
    nacionalidad = models.CharField(max_length=20, null=True, blank=True)
    localidad = models.CharField(max_length=50, null=True, blank=True)
    codigo_postal = models.BigIntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    disponibilidad_viajar = models.BooleanField(null=True, blank=True)
    disponibilidad_mudarse = models.BooleanField(null=True, blank=True)
    movilidad_propia = models.BooleanField(null=True, blank=True)
    perfil = models.TextField(null=True, blank=True)
    habilidades = models.TextField(null=True, blank=True)
    imagen = models.FileField(null=True, blank=True)

    # Array de licencias de conducir
    licencias = ArrayField(
        models.CharField(max_length=5),
        null=True,
        default=licencia_default
    )

    # Array de experiencias laborales
    experiencia = ArrayField(
        HStoreField(),
        null=True,
        blank=True
    )

    # Array de estudios
    estudios = ArrayField(
        HStoreField(),
        null=True,
        blank=True
    )

    # Indica si el CV está lo suficientemente completo como para postularse a las ofertas
    completo = models.BooleanField(default=False, null=True, blank=True)

    # cv = CV.objects.create(nombre="Lautaro Lopez", DNI=40267609, fecha_nacimiento="09/01/1997", genero="Hombre", nacionalidad="AR", localidad="Santa Fe", codigo_postal=3000, direccion="Alvear 7729", telefono=3425080015, email="lauty@mail.com", disponibilidad_viajar=False, disponibilidad_mudarse=False, movilidad_propia=False, perfil="xd", habilidades="xd", licencias=["No Posee"], experiencia=[{"empresa": "La empresa"}], estudios=[{"institucion": "Escuela"}], completo=True)