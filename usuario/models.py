from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Usuario(models.Model):
	usuario_id = models.AutoField(auto_created=True, primary_key=True, editable=False)
	nombre = models.CharField(max_length=60)
	telefono = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	contrasena = models.CharField(max_length=20)
	domicilio = models.CharField(max_length=100)
"""

class Visitante(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	telefono = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=100)

	def __str__(self):
		return "{} - {}".format(self.usuario.first_name, self.usuario.email)

class Producto(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField()
	precio = models.FloatField()
