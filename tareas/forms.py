from django import forms
from .models import Comentario, Tarea, Categoria
from pagedown.widgets import PagedownWidget

# creo un formulario con el campo texto para mostrar
class Comentarios(forms.ModelForm):

    texto = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Comentario
        fields=['texto']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
		    fields = ['titulo', 'descripcion', 'categoria', 'prioridad']   
