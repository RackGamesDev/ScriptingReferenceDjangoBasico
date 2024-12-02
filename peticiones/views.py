from django.shortcuts import render
from django.http import HttpResponse
import json

def pruebas(request):
    return render(request, 'peticiones/index.html', {})

def recibePeticion(request):
    print(request.method) #El verbo de la peticion http
    print(request.COOKIES) #Las cookies de la peticion
    print(request.path) #Destino de la peticion
    print(request.FILES) #En caso de haber enviado archivos, aparecen aqui
    print(request.META) #Muchos datos del cliente

    data = request.body
    data = str(data, encoding='utf-8')
    data = json.loads(data)
    print(data['texto']) #El body en formato dictionary de python
    print(data['objeto']['nombre'])

    return HttpResponse(json.dumps({"respuesta": "bien", "objeto": {"propiedad": 34}})) #Para devolver un json
