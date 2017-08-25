from django import forms
from .models import Comentario,Tarea,Categoria

# creo un formulario con el campo texto para mostrar
class ComentarioForm(forms.ModelForm):
	class Meta:

		model= Comentario
		fields=['texto']

class TareaForm(forms.ModelForm):
	class Meta:
		model = Tarea
		fields = ['titulo','descripcion','categoria','prioridad']
		
	
	
   
