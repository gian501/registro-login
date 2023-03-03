from django.urls import path
from .views import home, products, register, aboutus, busquedaProducto,buscar
from Core import views
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('aboutus/', aboutus, name='aboutus'),
    path('busquedaProducto', busquedaProducto, name= "busquedaProducto"),
    path('buscar/', buscar),

    path('producto/list', views.ProductoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete')
]