import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200 )
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):   
    id_categoria = models.IntegerField( primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500) 
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
    
    def __str__(self):
        return self.nombre        
    
class Producto(models.Model):   
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id = models.IntegerField( primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
    imagen = models.ImageField()
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
            return self.nombre    
    
    @property 
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    


 
   