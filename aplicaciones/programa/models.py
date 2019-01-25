from django.db import models

from aplicaciones.agregar.models import Persona


class Extensiones(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


class Programa(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    version = models.IntegerField()
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    extensiones = models.ManyToManyField(Extensiones, blank=True)
