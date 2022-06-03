from dataclasses import fields
from django import forms
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
    class Meta:
        model = User
        fields = ['username', "email", "password1", "password2"]