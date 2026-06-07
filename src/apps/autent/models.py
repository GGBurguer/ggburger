from django.db import models

# Modelo de datos simple para la autenticación de los usuarios


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_us = models.CharField(max_length=16, null=False)
    contr_us = models.CharField(
        max_length=150, null=False
    )  # La contraseña estaría hasheada
