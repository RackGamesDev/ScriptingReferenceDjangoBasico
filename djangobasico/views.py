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
