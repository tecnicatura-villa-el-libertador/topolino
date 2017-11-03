from django.db import models
from django.utils import timezone
from pagedown.widgets import PagedownWidget
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    asignado = models.ForeignKey(User,null=True,related_name="tareas_asignada",limit_choices_to={'is_staff':True})

    def __str__(self):
        return self.titulo


    @property
    def esta_finalizado(self):
        return self.estado == Tarea.FINALIZADO

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
      manual = models.BooleanField(default= True)


@receiver(post_save)
def my_callback(sender, instance, **kwargs):
    print("llego señal post save", instance)
