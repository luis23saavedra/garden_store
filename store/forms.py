from dataclasses import fields
from django import forms
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError




class ProductoForm(forms.ModelForm):
    
    #validadores en los formularios
    id = forms.IntegerField(min_value=1, max_value=100)
    nombre = forms.CharField(min_length=3)
    precio = forms.IntegerField(min_value=1000, max_value=100000)
    
    #def clean_nombre(self):
     #   nombre = self.cleaned_data["nombre"]
      #  existe = Producto.objects.filter(nombre=nombre).exists()
       # 
        #if existe:
         #   raise ValidationError("Nombre ya en uso")
        
       # return nombre
    
    class Meta:
        model = Producto
        fields = '__all__'
        
class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3)
    email = forms.EmailField(max_length=50, widget=forms.EmailInput, label="Email")
    class Meta:
        model = Cliente
        fields = '__all__'        
        
        
##se importa usercreationform y genera automaticamente el formulaio para registrar un usuario y asi no hay que crear superuser         
class CustomerUserCreationForm(UserCreationForm):  
    
    class Meta:
        model = User
        fields = ['username', "email", "password1", "password2"]