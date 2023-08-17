from django.db import models

# Create your models here.

class Integrante(models.Model):
    nombre = models.CharField(max_length=100)

class Audio(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.DurationField()

