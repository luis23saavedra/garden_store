from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', views.ProductoViewSet)
router.register('cliente', views.ClienteViewSet)
router.register('suscriptor', views.SuscriptorViewSet)

urlpatterns = [
     path('', views.home, name="home"),
     path('cart/', views.cart, name="cart"),
     path('tienda/', views.store, name="store"),
     path('checkout/', views.checkout, name="checkout"),
     path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
     path('agregar_suscriptor/', views.agregar_suscriptor, name="agregar_suscriptor"),
     path('listar/', views.listar, name="listar"),
     path('editar_producto/<id>/', views.editar_producto, name="editar_producto"),
     path('eliminar_producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
     path('listar_cliente/', views.listar_cliente, name="listar_cliente"),
     path('agregar_cliente/', views.agregar_cliente, name="agregar_cliente"),
     path('registro/', views.registro, name="registro"),
     path('api/', include(router.urls)),
     
     
]
