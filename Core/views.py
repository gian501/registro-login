from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from Core.models import Producto
#from Core.forms import ProductoFormulario


# Create your views here.

def home(request):
    return render(request, 'Core/home.html')

@login_required
def products(request):
    producto = Producto.objects.all()
    return render(request, 'Core/products.html', {'producto':producto})

class ProductoList(ListView):
    model = Producto
    template_name = "Core/producto_list.html"
    
class ProductoDetalle(DetailView):
    model = Producto
    template_name = "Core/producto_detalle.html"
    
class ProductoCreacion(CreateView):
    model = Producto
    success_url = "/Core/producto/list"
    fields = ['nombre', 'precio', 'cantidad', 'imagen']

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = "/Core/producto/list"
    fields = ['nombre', 'precio', 'cantidad', 'imagen'] 
    
class ProductoDelete(DeleteView):
    model = Producto
    success_url = "/Core/producto/list"




def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', data)

def aboutus(request):
    return render(request, 'Core/aboutus.html')

def busquedaProducto(request):
    return render(request, "Core/busquedaProducto.html" )

def buscar(request):
    if request.GET['nombre']:
        nombre = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "Core/resultadoBusqueda.html", {"nombre":nombre})
    else:
        respuesta = "No enviaste datos"
    
    #return render(request, 'AppC/inicio.html',{"respuesta": respuesta})
    return HttpResponse(respuesta)







'''def productos(request):
    if request.method == "POST":
 
        miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(nombre=informacion["producto"], precio=informacion["precio"], cantidad=informacion["Cantidad"],Imagen=informacion["Imagen"])
            producto.save()
            #return render(request, "AppE03/cursos.html") #ubicacion a donde me lleva
            return render(request, "Core/home.html")
    else:
        miFormulario = ProductoFormulario()
        
    return render(request, 'Core/products.html', {"miFormulario":miFormulario})'''