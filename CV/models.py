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
    no_posee = ['No Posee']
    return list(no_posee)
# Función para setear por defecto como arreglo vacio los arreglos de Experiencia y Estudios
def arreglo_vacio():
    return(list())

# Create your models here.
class CV(models.Model):

    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    DNI = models.BigIntegerField(null=True)
    fecha_nacimiento = models.CharField(max_length=15, null=True)
    genero = models.CharField(max_length=15, null=True)
    nacionalidad = models.CharField(max_length=20, null=True)
    localidad = models.CharField(max_length=50, null=True)
    codigo_postal = models.BigIntegerField(null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.BigIntegerField(null=True)
    email = models.EmailField(null=True)
    disponibilidad_viajar = models.BooleanField(null=True, blank=True)
    disponibilidad_mudarse = models.BooleanField(null=True, blank=True)
    movilidad_propia = models.BooleanField(null=True, blank=True)
    perfil = models.TextField(null=True, blank=True, default="")
    habilidades = models.TextField(null=True, blank=True, default="")
    imagen = models.ImageField(upload_to="profile_pics",null=True, blank=True, default='profile_pics/fotocv.png')

    # Array de licencias de conducir
    licencias = ArrayField(
        models.CharField(max_length=10),
        null=True,
        default=licencia_default
    )

    # Array de idiomas
    idiomas = ArrayField(
        HStoreField(),
        null=True,
        blank=True,
        default=arreglo_vacio
    )

    # Array de experiencias laborales
    experiencia = ArrayField(
        HStoreField(),
        null=True,
        blank=True,
        default=arreglo_vacio
    )

    # Array de estudios
    estudios = ArrayField(
        HStoreField(),
        null=True,
        blank=True,
        default=arreglo_vacio
    )

    # Indica si el CV está lo suficientemente completo como para postularse a las ofertas
    completo = models.BooleanField(default=False, null=True, blank=True)