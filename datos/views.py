from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Publicacion #importando el modelo de datos para la base de datos

# Create your views here.

def test(request):
    return HttpResponse("OK")

def create(request):
    usuario = Usuario(nombre="prueba", dinero=0, activo=True, descripcion="") #creando un objeto segun el modelo, tambien se puede crear con Usuario.objects.create(x)
    usuario.save() #guardandolo en la base de datos (con la otra manera no haria falta)
    return HttpResponse("OK")

def delete(request):
    usuario = Usuario.objects.get(id=1) #este buscaria el id para conseguir el registro (tambien se puede recibir con Usuario.objects.filter(id=x))
    usuario.delete() #y lo borra de la base de datos
    return HttpResponse("OK")

def consultas(request):
    usuarios = Usuario.objects.all() #devuelve todas las entradas
    return render(request, 'datos/consultas.html', {'usuarios': usuarios})
