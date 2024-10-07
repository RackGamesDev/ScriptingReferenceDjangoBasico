from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),#esta url seria accesibles en dominio.x/datos/test
    path('create/', views.create, name="create"),
    path('delete/', views.delete, name="delete"),
    path('consultas/', views.consultas, name="consultas"),
    path('actualizacion/', views.actualizacion, name="actualizacion"),

]