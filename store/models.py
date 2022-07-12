
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200 )
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    
class Suscriptor(models.Model):   
    id_suscriptor = models.IntegerField( primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500) 
    plan = models.CharField(max_length=20) 
    creado= models.DateTimeField(auto_now_add=True) 
    modificado= models.DateTimeField(auto_now_add=True)     
    
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
    precio = models.IntegerField()
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
    
class Order (models.Model):
    customer = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    completo = models.BooleanField(default=False)
    id_transaccion = models.CharField( max_length=100)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitem= self.orderitem.all()
        total = sum([item.get_total for item in orderitem]) 
        return total
    
    @property
    def get_cart_productos(self):
        productosorden= self.detalleorden_set.all()
        total = sum([item.cantidad for item in productosorden]) 
        return total
    
    
class OrderItem(models.Model):
    product= models.ForeignKey(Producto, on_delete=models.CASCADE)
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    fecha_do = models.DateTimeField(auto_now_add=True)    
    
    @property
    def get_total(self):
        total = self.product.precio * self.quantity
        return total


 
    