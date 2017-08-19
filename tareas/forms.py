from django import forms
from .models import Comentario
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.models import User

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