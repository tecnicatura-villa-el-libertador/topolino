from django import forms
from .models import Comentario

# creo un formulario con el campo texto para mostrar
class Comentarios(forms.ModelForm):
	class Meta:
		model= Comentario
		fields=['texto']
   
