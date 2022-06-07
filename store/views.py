from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import ClienteForm, CustomerUserCreationForm, ProductoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, ClienteSerializer




# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer     


def home(request):
    
    return render(request, 'store/home.html')


def store(request):
    products = Producto.objects.all()
    context = {'products': products}
    return render(request, 'store/tienda.html', context)

def cart(request):
    
    if request.user.is_authenticated:
      Cliente= request.user.cliente
      
      
   
    return render(request, 'store/cart.html')

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


@permission_required('store.add_producto')
def agregar_producto(request):
    
    data= {
        'producto_form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
            data["mensaje"] = "guardado"
        else:
            data ["form"] = formulario
    
    return render (request, 'store/agregar_producto.html', data)

@permission_required('store.add_producto')
def listar(request):
    
    products = Producto.objects.all()
    
    data = {
        'products' : products
    }
    
    return render(request, 'store/listar.html', data)


@permission_required('store.add_producto')
def editar_producto(request, id):
    
    producto = get_object_or_404(Producto, id = id)
    data = {
        'form': ProductoForm(instance = producto)
    }
    
    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listar")
        data['producto_form']= formulario
      
    return render(request, 'store/editar_producto.html', data)


@permission_required('store.add_producto')
def eliminar_producto(request, id):
    products= get_object_or_404(Producto, id= id)
    products.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="listar")


@permission_required('store.add_producto')
def listar_cliente(request):
    
    clientes = Cliente.objects.all()
    
    data = {
        'clientes' : clientes
    }
    
    return render(request, 'store/listar_cliente.html', data)



def agregar_cliente(request):
    
    data= {
        'cliente_form': ClienteForm()
    }
    
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado"
        else:
            data ["form"] = formulario
    
    return render (request, 'store/agregar_cliente.html', data)

def registro(request):
    data = {
        'form': CustomerUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario =CustomerUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            Cliente.objects.create(user=user, nombre=user.username, email=user.email)
            login(request, user)
            messages.success(request, "Registro con éxito ahora puedes comprar en nuestra tienda")
            return redirect(to="store")
        data["form"] = formulario
    
    
    return render(request, 'registration/registro.html',data)
