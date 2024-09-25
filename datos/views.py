from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario #importando el modelo de datos para la base de datos

# Create your views here.

def test(request):
    return HttpResponse("OK")

def create(request):
    usuario = Usuario(nombre="prueba", dinero=0, activo=True, descripcion="") #creando un objeto segun el modelo
    usuario.save() #guardandolo en la base de datos
    return HttpResponse("OK2")
