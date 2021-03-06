from django.contrib import admin
from .models import Categoria, Producto,  Cliente, Order, OrderItem, Suscriptor
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Suscriptor)







class CategoriaProAdmin(admin.ModelAdmin):
    
    readonly_fields=("creado", "modificado")

class ProductoAdmin(admin.ModelAdmin):
    
    readonly_fields=("creado", "modificado")   
    
admin.site.register(Categoria, CategoriaProAdmin)  
admin.site.register(Producto, ProductoAdmin)   
    
    

