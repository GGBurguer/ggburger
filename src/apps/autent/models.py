from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de datos simple para la autenticación de los usuarios

# Los tipos de usuarios se van a representar en diferentes clases relacionadas con la clase general usuario,
# ya que es de esta unica que puede leer django para las funciones de autenticación y validación


# Entidad general de usuarios
class Usuario(AbstractUser):
	id = models.BigAutoField(primary_key=True)
	# nombre_us = models.CharField(max_length=16, null=False)
	# contr_us = models.CharField(
	# 	max_length=150, null=False
	# )  # La contraseña estaría hasheada


# Entidad de usuarios cocineros
class Cocinero(models.Model):
	# id = models.BigAutoField(primary_key=True)
	nombre = models.CharField(max_length=20, null=False)
	apellido = models.CharField(max_length=20, null=False)
	# fecha_nacimiento
	# dni = models.CharField
	us = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
