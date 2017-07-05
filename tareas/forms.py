from django import forms
from .models import Comentario

class Comentarios(forms.ModelForm):
	class Meta:
		model= Comentario
		fields=['nombre','texto']
   
