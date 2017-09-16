from django.db import models
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from django.contrib.auth.models import User


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
    descripcion = models.TextField(max_length=1000)
    fecha_creacion = models.DateField((), auto_now_add = True)
    estado = models.CharField(max_length=15, choices=RANGO_DE_ESTADOS,default=PENDIENTE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return '/tareas/{}/'.format(self.id)

# Create your models here.

class Categoria(models.Model):
      nombre = models.CharField(max_length = 200)

      def __str__(self):
          return self.nombre

class Comentario(models.Model):
      tarea = models.ForeignKey(Tarea, null=True)
      usuario = models.ForeignKey(User)
      fecha = models.DateTimeField(default= timezone.now)
      texto = models.TextField()



