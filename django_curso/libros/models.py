from django.db import models

# Create your models here.

class Libro(models.Model) :
    GENEROS = [(1, 'Novela'), (2, 'Ensayos')]
    titulo = models.CharField(max_length=100)
    autor = models.ManyToManyField('Autor', blank=True)
    anio = models.CharField(max_length=10)
    editorial = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    genero = models.IntegerField(choices=GENEROS, blank=True)

class Autor(models.Model):
    apellidos = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100, blank=True)
    fecha_nacim = models.DateField()