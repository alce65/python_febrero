from django.contrib import admin
from .models import Libro, Autor
# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['apellidos', 'nombre', 'fecha_nacim']