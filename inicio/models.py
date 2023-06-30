from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()

    def __str__(self):
        return self.modelo

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return self.nombre
