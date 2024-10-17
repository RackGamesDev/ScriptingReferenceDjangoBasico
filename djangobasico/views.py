from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):#esta funcion es asignable a una url en urls.py y recibe request (de la peticion http)
    return HttpResponse("hola")#y simplemente devuelve como http este texto

def suma(request, a, b, c):#la funcion de esta url recibe variables, en este caso tipo int y str
    return HttpResponse(str(a + b) + c)

def pagina(request):
    return render(request, 'pagina.html', {})#enviar un html desde una url (poner la url a partir de la asociada en settings.py)

def dinamico(request, texto):
    cosas = ['234', 'sdfgas', 'asdf']
    return render(request, 'dinamico.html', {'texto': texto, 'cosas': cosas})#pasandole los parametros al html

def estaticos(request):
    return render(request, 'estaticos.html', {})

def herencia(request):
    return render(request, 'herencia.html', {})

def index(request):
    return render(request, 'index.html', {})

def formularios(request):
    return render(request, 'formularios.html', {})

def destinoformularioget(request):
    if request.method == 'GET': #el metodo de la peticion http (GET, POST, DELETE, PUT...)
        nombre = request.GET['mensaje'] #en caso de que sea ese tipo de peticion, recoger cada dato enviado por fomulario
        #al ser get, los datos vienen en la url asi que se recogen de aqui
    return render(request, 'destinoformularioget.html', {'nombre': nombre})

def destinoformulariopost(request):
    if request.method == 'POST':
        nombre = request.POST['nombre'] #recibiendo los datos de la peticion post
        numero = request.POST['numero']
    return render(request, 'destinoformulariopost.html', {'nombre': nombre, 'numero': numero})
