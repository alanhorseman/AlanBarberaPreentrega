from django.db import models
from decimal import Decimal
# Create your models here.

class ProductoCategoria(models.Model):
    '''Categorias de productos'''
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.PositiveIntegerField(null=False, blank=False, unique=True, default=1)
    puntos = models.PositiveIntegerField(blank=True, default=1)
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="descripción")
    precio_revista = models.DecimalField(max_digits=300, decimal_places=2, default=Decimal('0.00'))
    # precio_consultora = models.DecimalField(max_digits=300, decimal_places=2)

    def __str__(self):
        '''Representa una instacia del modelo como una cadena de texto'''
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría de productos"
        verbose_name_plural = "Categorías de productos"