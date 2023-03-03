from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Curso'}))
    precio = forms.FloatField()
    cantidad = forms.IntegerField()
    imagen = forms.ImageField()