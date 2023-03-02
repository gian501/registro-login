from django.contrib import admin
#from .models import Profile
from .models import *

# Register your models here.

#admin.site.register(Profile)

'''admin.site.register(Producto)'''

class ProductoAdmin(admin.ModelAdmin):
    list_display =('nombre','precio','cantidad')

admin.site.register(Producto, ProductoAdmin)