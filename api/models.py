from django.db import models 
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Person(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 200)
    foto = models.ImageField(null=True, blank=True, upload_to='fotos/')
    class Meta:
        abstract = True

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True, upload_to='categorias/')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    productoName = models.CharField(max_length=200)
    productoDescription = models.CharField(blank=True, max_length=200)
    productoPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productoImage = models.ImageField(null=True, blank=True, upload_to='images/')
    productoCantidad = models.PositiveBigIntegerField(default=0) 
    productoCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    # create_at = models.DateTimeField(default=datetime.datetime.now)
    def __str__ (self):
        return self.productoName