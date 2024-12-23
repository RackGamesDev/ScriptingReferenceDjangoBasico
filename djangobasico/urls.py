"""
URL configuration for djangobasico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from . import views #IMPORTANTE IMPORTAR ESTO

urlpatterns = [
    path('admin/', admin.site.urls), #Panel de administracion de django
    path('saludo/', views.saludo, name='saludo'),#Poner esto por cada url posible, en este caso llama a la funcion saludo de views.py
    path('suma/<int:a>/<int:b>/<str:c>/', views.suma, name='suma'),#Cuando la url tenga variables (suma/3/5/hola)
    path('pagina/', views.pagina, name='pagina'),#Esta devuelve un html (template)
    path('dinamico/<str:texto>', views.dinamico, name='dinamico'),#Esta representa la variable en el html con parametros
    path('estaticos/', views.estaticos, name='estaticos'),#Esta pagina tiene archivos estaticos
    path('herencia/', views.herencia, name='herencia'),#Este html es una extension de otro que es una plantilla
    path('', views.index, name='index'),#Esta es la pagina principal
    path('datos/', include('datos.urls')),#Esta conecta con una view de otro modulo (hace falta importar include) (dominio.x/datos/test)
    path('formularios/', views.formularios, name="formularios"), #Usados para formularios normales
    path('destinoformularioget/', views.destinoformularioget, name="destinoformularioget"),
    path('destinoformulariopost/', views.destinoformulariopost, name="destinoformulariopost"),
    path('formsdjango/', views.formsdjango, name='formsdjango'), #Usado para formularios de django
    path('formsdjangodestino/', views.formsdjango, name='formsdjangodestino'),
    path('peticiones/', include('peticiones.urls')),
    
]
