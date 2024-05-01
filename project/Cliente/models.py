from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=100, blank=True, verbose_name= "País")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Países"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Usuarios"

class MetodosPagos(models.Model):
    tarjeta = models.CharField(max_length=150, verbose_name="Tipo de tarjeta")

    def __str__(self):
        return f"{self.tarjeta}"
    
    class Meta:
        verbose_name_plural = "Metodos Pagos"