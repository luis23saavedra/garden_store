import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):    
    id = models.IntegerField( primary_key=True)
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField()
    stock = models.BooleanField(default=True, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    
def __str__(self):
        return self.nombre    
    
@property 
def imageURL(self):
    try:
        url = self.image.url
    except:
        url = ''
    return url
    
    
    
    
    
class Boleta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)   
    fecha = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=True)
    id_transaccion = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)

class DetalleBoleta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_db = models.DateTimeField(auto_now_add=True) 
    
class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)   
    boleta = models.ForeignKey(Boleta, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    comuna = models.CharField(max_length=200, null=True)
    fecha_de = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion
 
   