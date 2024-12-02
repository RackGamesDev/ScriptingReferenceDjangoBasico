from django.http import HttpResponse
from django.shortcuts import render
from .forms import ComentarioForm #Para el formulario de django

def saludo(request):#Esta funcion es asignable a una url en urls.py y recibe request (de la peticion http)
    return HttpResponse("hola")#Y simplemente devuelve como http este texto

def suma(request, a, b, c):#La funcion de esta url recibe variables, en este caso tipo int y str
    return HttpResponse(str(a + b) + c)

def pagina(request):
    return render(request, 'pagina.html', {})#Enviar un html desde una url (poner la url a partir de la asociada en settings.py)

def dinamico(request, texto):
    cosas = ['234', 'sdfgas', 'asdf']
    return render(request, 'dinamico.html', {'texto': texto, 'cosas': cosas})#Pasandole los parametros al html

def estaticos(request):
    return render(request, 'estaticos.html', {})

def herencia(request):
    return render(request, 'herencia.html', {})

def index(request):
    return render(request, 'index.html', {})

def formularios(request):
    return render(request, 'formularios.html', {})
def destinoformularioget(request):
    if request.method == 'GET': #El metodo de la peticion http (GET, POST, DELETE, PUT...)
        nombre = request.GET['mensaje'] #En caso de que sea ese tipo de peticion, recoger cada dato enviado por fomulario
        #Al ser get, los datos vienen en la url asi que se recogen de aqui
    return render(request, 'destinoformularioget.html', {'nombre': nombre})
def destinoformulariopost(request):
    if request.method == 'POST':
        nombre = request.POST['nombre'] #Recibiendo los datos de la peticion post
        numero = request.POST['numero']
    return render(request, 'destinoformulariopost.html', {'nombre': nombre, 'numero': numero})

def formsdjango(request): #En este caso estan tanto el destino del fofmulario como el formulario en la misma funcion
    if request.method == 'GET':
        comentarioForm = ComentarioForm({'nombre': 'por defecto'}) #Usando el formulario de django hecho en forms.py, se pueden especificar valores iniciales
        return render(request, 'formsdjango.html', {'comentairoForm': comentarioForm})
    elif request.method == 'POST':
        comentarioForm = ComentarioForm(request.POST) #Recibiendo el resultado del formulario para validarlo
        if comentarioForm.is_valid(): #Si es completamente valido
            return HttpResponse(request.POST['nombre'] + str(request.POST['numero']))
        else:
            return HttpResponse("error")
