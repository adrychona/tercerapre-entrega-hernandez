from django.db import models

# Create your models here.

class Mascota(models.Model):
   
    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()


class Vacuna(models.Model):
    
    mascota = models.CharField(max_length=40)
    vacuna = models.CharField(max_length=40)
    fecha = models.DateField()


class Consulta(models.Model):
    
    paciente = models.CharField(max_length=40)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    vet = models.CharField(max_length=40)
    establecimiento = models.CharField(max_length=100)

