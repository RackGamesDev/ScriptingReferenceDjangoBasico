from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Publicacion, Grupo #Importando el modelo de datos para la base de datos

# Create your views here.

def test(request):
    return HttpResponse("OK")

def create(request):
    usuario = Usuario(nombre="prueba", dinero=4, activo=True, descripcion="") #Creando un objeto segun el modelo, tambien se puede crear con Usuario.objects.create(x)
    usuario.save() #Guardandolo en la base de datos (con la otra manera no haria falta)
    publicacion = Publicacion(usuario=usuario, nombre="aa", puntuacion=1) #Creando objeto que requiere de otro mediante relacion (se puede especificar recibiendo el objeto desde la base de datos)
    grupo1 = Grupo(nombre="a1")
    grupo1.usuarios.add(usuario) #En caso de ser relacion muchos-muchos se agregan asi
    return HttpResponse("OK")

def delete(request):
    usuario = Usuario.objects.get(id=1) #Este buscaria el id para conseguir el registro (tambien se puede recibir con Usuario.objects.filter(id=x))
    usuario.delete() #Y lo borra de la base de datos
    return HttpResponse("OK")

def consultas(request):
    usuarios = Usuario.objects.all() #Devuelve todas las entradas
    usuarioEspecifico = Usuario.objects.filter(dinero=4, nombre='prueba').order_by('nombre') #Devuelve las entradas que cumplan esas condiciones, el order_by lo ordena segun un parametro
    unUsuario = Usuario.objects.get(id=1) #Devuelve una entrada especifica
    algunosUsuarios = Usuario.objects.all()[:3] #Como devuelve un array se puede limitar asi
    usuarioFiltro = Usuario.objects.filter(id__lte=2) #Condiciones especificas (__lte(menor/igual) __gte(mayor/igual) __lt(menor) __gt(mayor) __contains __exact)
    usuarioFiltro2 = Usuario.objects.filter(nombre__contains='pr')
    publicacion = Publicacion.objects.get(id=1)
    publicacion.usuario.nombre = "aa" #Accediendo a una propiedad de un objeto relacionado con este
    usuarioGrupo = Grupo.objects.get(id=1).usuarios.get(id=1) #Accediendo a un objeto desde otro con relacion muchos-muchos (estan los mismos metodos de filtrado)
    return render(request, 'datos/consultas.html', {'usuarios': usuarios})

def actualizacion(request):
    #Modificacion de datos sabiendo el id
    objeto = Usuario.objects.get(id=2)
    objeto.nombre = "otro"
    objeto.save()
    return HttpResponse("OK")
