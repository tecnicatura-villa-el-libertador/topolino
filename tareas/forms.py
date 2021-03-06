from django import forms
from .models import Comentario, Tarea, Categoria
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.models import User
from pagedown.widgets import PagedownWidget


# creo un formulario con el campo texto para mostrar
class Comentarios(forms.ModelForm):
      class Meta:
          model= Comentario
          fields=['texto']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        field_classes = {'username': UsernameField}

# creo un formulario con el campo texto para mostrar
class ComentarioForm(forms.ModelForm):

    texto = forms.CharField(label="", widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Comentario
        fields=['texto']

class TareaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad']

class Tarea_estado(forms.ModelForm):
	class Meta:
		model = Tarea
		fields= ['estado']

class BuscarForm(forms.Form):
	buscar= forms.CharField(max_length=50)






