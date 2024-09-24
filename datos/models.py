from django.db import models

# Create your models here.

#CADA VEZ QUE SE ACTUALICE ESTE ARCHIVO: python manage.py makemigrations ; python manage.py migrate

class Usuario(models.Model):#creando un modelo para un objeto de la base de datos
    nombre = models.CharField(max_length=12, null=False, default="a")#sus propiedades y como funcionan (automaticamente traducidas a sql)
    dinero = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)
    descripcion = models.TextField(default="", null=True)
    fecha = models.DateField(null=True)

    def __str__(self):
        return
