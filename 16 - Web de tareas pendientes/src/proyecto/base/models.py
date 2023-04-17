'''
La definicion de los datos almacenados, en forma de clases
'''

from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    usuario = models.ForeignKey(User, 
                                on_delete=models.CASCADE, #si se elimina usuario tambien sus tareas
                                null=True, #puede estar vacio
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True) #se a;ade fecha automaticamente

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']

    
