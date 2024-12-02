from django.db import models
from datetime import date

# Create your models here.

#CADA VEZ QUE SE ACTUALICE ESTE ARCHIVO: python manage.py makemigrations ; python manage.py migrate

class Usuario(models.Model):#Creando un modelo para un objeto de la base de datos
    nombre = models.CharField(max_length=12, null=False, default="a")#sus propiedades y como funcionan (automaticamente traducidas a sql)
    dinero = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)
    descripcion = models.TextField(default="", null=True)
    fecha = models.DateField(null=True, default=date.today)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)#Clave foranea para relacionar entidades (la publicacion pertenece a un usuario) (se podrian hacer relaciones 1:1, 1:n y n:m segun como se hagan las claves)
    nombre = models.CharField(max_length=10, null=False, default="a")
    puntuacion = models.FloatField(null=False, default=0.4)
    def __str__(self):
        return self.usuario.nombre #Accediendo a las propiedades de un objeto conectado

class Grupo(models.Model):
    nombre = models.CharField(max_length=10, null=False, default="a")
    usuarios = models.ManyToManyField(Usuario) #Para relaciones muchos-muchos, esto crearia una tabla extra en sql (se puede hacer manualmente con otro modelo)
    def __str__(self):
        return self.nombre
