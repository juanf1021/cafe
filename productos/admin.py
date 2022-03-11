from asyncore import read
from django.contrib import admin
from .models import Productos, Categoria, Menu
# Register your models here.


class Producto_admin(admin.ModelAdmin):
    readonly_fields=('creado',)

admin.site.register(Productos, Producto_admin)

class Categoria_admin(admin.ModelAdmin):
    readonly_fields=('creado',)

admin.site.register(Categoria, Categoria_admin)

class Menu_admin(admin.ModelAdmin):
    readonly_fields= ('creacion',)

admin.site.register(Menu, Menu_admin)