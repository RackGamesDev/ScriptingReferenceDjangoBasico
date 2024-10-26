from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pruebas/', views.pruebas, name="pruebas"),
    path('recibePeticion/', views.recibePeticion, name="recibePeticion"),

]