

from django.contrib.auth.models import AbstractUser # AbstractUser para extender el modelo de usuario predeterminado de Django
from django.db import models

class User(AbstractUser):
    #  roles en el sistema
    class Roles(models.TextChoices):
        EMPRENDEDOR = 'EMPRENDEDOR', 'Emprendedor'
        ADMIN_ALCALDIA = 'ADMIN', 'Administrador Alcaldía'

    role = models.CharField(
        max_length=20, 
        choices=Roles.choices, 
        default=Roles.EMPRENDEDOR
    )
    telefono = models.CharField(max_length=15, blank=True, null=True)
    documento_identidad = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"# Create your models here.
