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
        return reverse_lazy('proyecto:lista')
