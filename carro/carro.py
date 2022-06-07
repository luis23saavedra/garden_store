from django.urls import clear_script_prefix


class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.Session
        carro=self.session.get("carro")
        if not carro:
            carro.self.session["carro"]={}
        else:
            self.carro=carro
            
    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }        