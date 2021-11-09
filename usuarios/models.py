from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    
    datos = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.tipo_cuenta}'