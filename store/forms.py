from dataclasses import fields
from django import forms
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'        
        
        
##se importa usercreationform y genera automaticamente el formulaio para registrar un usuario y asi no hay que crear superuser         
class CustomerUserCreationForm(UserCreationForm):  
    pass      