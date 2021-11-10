from django.db import models
from django.contrib.auth.models import User
from CV.models import CV

# Create your models here.
class UserProfile(models.Model):
    
    datos = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=15)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.datos.username} - {self.tipo_cuenta}'