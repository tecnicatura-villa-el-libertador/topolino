from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
      nombre = models.CharField(max_length = 200)

      def __str__(self):
          return self.nombre
class Comentario(models.Model):
      nombre = models.CharField(max_length = 200)
      fecha = models.DateTimeField(default= timezone.now)
      texto = models.TextField()
   
