from django.db import models
from django.utils import timezone

# Create your models here.

class CaseInsensitiveCharField(models.CharField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            return value.lower()
        return value

class Pais(models.Model):
    nombre = CaseInsensitiveCharField(max_length=100, verbose_name="País", unique=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Países"

class MetodosPagos(models.Model):
    tarjeta = models.CharField(max_length=150, verbose_name="Tipo de tarjeta")

    def __str__(self):
        return self.tarjeta
    
    class Meta:
        verbose_name_plural = "Metodos Pagos"

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tarjeta_id = models.ForeignKey(MetodosPagos, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Pago") #ingrese esta linea
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="País")
    fecha = models.DateTimeField(default=timezone.now, null=True, blank=True, editable=False, verbose_name= "Última actualización")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Usuarios"