from django.urls import path
from tienda import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('tienda/', views.tienda, name="tienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('pagar/', views.pagar, name="pagar"),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('listar/', views.listar, name="listar"),
    path('editar_producto/<id>/', views.editar_producto, name="editar_producto"),
    path('eliminar_producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('listar_cliente/', views.listar_cliente, name="listar_cliente"),
    path('agregar_cliente/', views.agregar_cliente, name="agregar_cliente"),
    path('registro/', views.registro, name="registro"),
    
]