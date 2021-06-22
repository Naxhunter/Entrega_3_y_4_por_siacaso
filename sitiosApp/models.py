from django.db import models

# Create your models here.
class CategoriaUnormal(models.Model):
    email= models.CharField(primary_key=True, max_length=30)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
class CategoriaUtrabajador(models.Model):
    rut= models.CharField(primary_key=True,max_length=30)
    email= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)
    telefono= models.IntegerField()
    def __str__(self):
        return self.nombre


