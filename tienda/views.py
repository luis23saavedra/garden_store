from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'tienda/home.html')

def tienda(request):
    
    return render(request, 'tienda/tienda.html')

def carrito(request):
    
    return render(request, 'tienda/carrito.html')

def pagar(request):
    
    return render(request, 'tienda/pagar.html')

def agregar_producto(request):
    
    return render(request, 'tienda/agregar_producto.html')

def listar(request):
    
    return render(request, 'tienda/listar.html')

def editar_producto(request):
    
    return render(request, 'tienda/editar_producto.html')

def eliminar_producto(request):
    
    return render(request, 'tienda/eliminar_producto.html')

def agregar_cliente(request):
    
    return render(request, 'tienda/agregar_cliente.html')

def listar_cliente(request):
    
    return render(request, 'tienda/listar_cliente.html')

def registro(request):
    
    return render(request, 'tienda/registro.html')




"""
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
            login(request, user)
            messages.success(request, "Registro con éxito ahora puedes comprar en nuestra tienda")
            return redirect(to="store")
        data["form"] = formulario
    
    
    return render(request, 'registration/registro.html',data)"""