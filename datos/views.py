from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Publicacion #importando el modelo de datos para la base de datos

# Create your views here.

def test(request):
    return HttpResponse("OK")

def create(request):
    usuario = Usuario(nombre="prueba", dinero=4, activo=True, descripcion="") #creando un objeto segun el modelo, tambien se puede crear con Usuario.objects.create(x)
    usuario.save() #guardandolo en la base de datos (con la otra manera no haria falta)
    return HttpResponse("OK")

def delete(request):
    usuario = Usuario.objects.get(id=1) #este buscaria el id para conseguir el registro (tambien se puede recibir con Usuario.objects.filter(id=x))
    usuario.delete() #y lo borra de la base de datos
    return HttpResponse("OK")

def consultas(request):
    usuarios = Usuario.objects.all() #devuelve todas las entradas
    usuarioEspecifico = Usuario.objects.filter(dinero=4, nombre='prueba').order_by('nombre') #devuelve las entradas que cumplan esas condiciones, el order_by lo ordena segun un parametro
    unUsuario = Usuario.objects.get(id=1) #devuelve una entrada especifica
    algunosUsuarios = Usuario.objects.all()[:3] #como devuelve un array se puede limitar asi
    usuarioFiltro = Usuario.objects.filter(id__lte=2) #condiciones especificas (__lte(menor/igual) __gte(mayor/igual) __lt(menor) __gt(mayor) __contains __exact)
    usuarioFiltro2 = Usuario.objects.filter(nombre__contains='pr')
    return render(request, 'datos/consultas.html', {'usuarios': usuarios})

def actualizacion(request):
    #modificacion de datos sabiendo el id
    objeto = Usuario.objects.get(id=2)
    objeto.nombre = "otro"
    objeto.save()
    return HttpResponse("OK")