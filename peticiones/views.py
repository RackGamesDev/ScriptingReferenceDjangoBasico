from django.shortcuts import render
from django.http import HttpResponse
import json

def pruebas(request):
    return render(request, 'peticiones/index.html', {})

def recibePeticion(request):
    print(request.method) #el verbo de la peticion http
    print(request.COOKIES) #las cookies de la peticion
    print(request.path) #destino de la peticion
    print(request.FILES) #en caso de haber enviado archivos, aparecen aqui
    print(request.META) #muchos datos del cliente

    data = request.body
    data = str(data, encoding='utf-8')
    data = json.loads(data)
    print(data['texto']) #el body en formato dictionary de python
    print(data['objeto']['nombre'])

    return HttpResponse(json.dumps({"respuesta": "bien", "objeto": {"propiedad": 34}})) #para devolver un json
