from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length = 255, blank = False, null = False)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(max_length=2083)


    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio} - Cantidad{self.cantidad}"
    