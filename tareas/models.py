from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    pass

class Tarea(models.Model):
    URGENTE=10
    MEDIA = 50
    BAJA = 100
    RANGO_DE_PRIORIDAD = ((URGENTE,'Urgente'),(MEDIA,'Medio'),(BAJA,'Baja'))
    INVALIDO = 'Invalido'
    EN_CURSO = 'En curso'
    PENDIENTE = 'Pendiente'
    FINALIZADO = 'Finalizado'
    RANGO_DE_ESTADOS = ((INVALIDO,'Invalido'),(EN_CURSO,'En curso'),(PENDIENTE,'Pendiente'),(FINALIZADO,'Finalizado'))
    usuario = models.ForeignKey(User)
    categoria = models.ForeignKey('Categoria')
    prioridad = models.IntegerField(choices=RANGO_DE_PRIORIDAD)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateField((), auto_now_add = True)
    estado = models.CharField(max_length=15, choices=RANGO_DE_ESTADOS)

class Comentario(models.Model):
    pass


