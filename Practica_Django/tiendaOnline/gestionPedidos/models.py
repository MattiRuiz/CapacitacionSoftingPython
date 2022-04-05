from encodings import search_function
from pyexpat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30, verbose_name="Nombre y apellido")
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField(blank=True, null=True) #Que no sea requerido
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return 'Cliente: %s - Dirección: %s' % (self.nombre, self.direccion)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'Artículo: %s | Sección: %s | Precio: %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()