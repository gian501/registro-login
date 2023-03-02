from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto
#from Core.models import Producto
#from Core.forms import ProductoFormulario


# Create your views here.

def home(request):
    return render(request, 'Core/home.html')

@login_required
def products(request):
    producto = Producto.objects.all()
    return render(request, 'Core/products.html', {'producto':producto})

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