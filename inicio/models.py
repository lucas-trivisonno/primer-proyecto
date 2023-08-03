from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    descripcion = RichTextField(null= True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"