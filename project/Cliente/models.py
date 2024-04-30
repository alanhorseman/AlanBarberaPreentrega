from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class MetodosPagos(models.Model):
    tarjeta = models.CharField(max_length=150)
    titular = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    numero_tarjeta = models.IntegerField(unique=True)
    cvv = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.tarjeta} de {self.titular}"