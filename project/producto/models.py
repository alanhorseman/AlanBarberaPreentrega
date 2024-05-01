from django.db import models

# Create your models here.

class ProductoCategoria(models.Model):
    '''Categorias de productos'''
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        '''Representa una instacia del modelo como una cadena de texto'''
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría de productos"
        verbose_name_plural = "Categorías de productos"

