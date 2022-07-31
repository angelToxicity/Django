from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.urls import reverse
# Create your models here.

class registro(models.Model):
    """
    Description: Modelo de Registro de Libro
    """
    SEXO = (
    	('F', 'F'),
    	('M', 'M'),
    )
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_publicacion = models.DateField()
    votos = models.IntegerField(null=True, blank= True)
    id_usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    resumen = models.CharField(max_length=500, default='')

    def get_absolute_url(self):
        return reverse_lazy('proyecto:lista-libros')


class productos(models.Model):
    """Description: Modelo de Registro de Productos"""
    titulo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, default=None)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('proyecto:lista')

class registro_producto(models.Model):
    """Description: Modelo de Registro de Productos"""
    producto = models.ForeignKey(productos, null=True, blank=True, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_recepcion = models.DateField()
    cantidad = models.IntegerField(null=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=100, default=None)
    lote = models.CharField(max_length=100, default=None)
