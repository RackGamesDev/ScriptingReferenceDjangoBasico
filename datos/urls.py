from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),#esta url seria accesibles en dominio.x/datos/test
    path('create/', views.create, name="create")
]