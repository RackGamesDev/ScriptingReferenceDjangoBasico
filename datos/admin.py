from django.contrib import admin
from .models import Publicacion

class PublicacionAdmin(admin.ModelAdmin): #para especificar mas como se mostrara un modelo en el panel
    list_display = ("usuario", "nombre", "puntuacion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)

# Register your models here.

admin.site.register(Publicacion, PublicacionAdmin) #cada modelo que aparecera en el panel de django (para poner ese filtro poner tambien el xAdmin)
