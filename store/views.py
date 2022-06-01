from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import ClienteForm, ProductoForm

# Create your views here.
def store(request):
    products = Producto.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    
    if request.user.is_authenticated:
      customer= request.user.cliente
      order, created = Boleta.objects.get_or_create(cliente= customer, completo=False)
      items= order.detalleboleta_set.all()
      
    else:
        items=[]
        
    context = {'items':items}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def agregar_producto(request):
    
    data= {
        'producto_form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado"
        else:
            data ["form"] = formulario
    
    return render (request, 'store/agregar_producto.html', data)

def listar(request):
    
    products = Producto.objects.all()
    
    data = {
        'products' : products
    }
    
    return render(request, 'store/listar.html', data)


def editar_producto(request, id):
    
    producto = get_object_or_404(Producto, id = id)
    data = {
        'form': ProductoForm(instance = producto)
    }
    
    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data['producto_form']= formulario
      
    return render(request, 'store/editar_producto.html', data)


def eliminar_producto(request, id):
    products= get_object_or_404(Producto, id= id)
    products.delete()
    return redirect(to="listar")


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