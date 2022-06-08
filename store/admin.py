from django.contrib import admin
from .models import Categoria, Producto,  Cliente
# Register your models here.
admin.site.register(Cliente)






class CategoriaProAdmin(admin.ModelAdmin):
    
    readonly_fields=("creado", "modificado")

class ProductoAdmin(admin.ModelAdmin):
    
    readonly_fields=("creado", "modificado")   
    
admin.site.register(Categoria, CategoriaProAdmin)  
admin.site.register(Producto, ProductoAdmin)   
    
    

