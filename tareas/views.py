from django.shortcuts import render,redirect
from .models import Categoria,Comentario,Tarea
from .forms import ComentarioForm, TareaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()

@login_required
def comentario(request):
    form = ComentarioForm()
   

    if request.method == "POST":

        form = ComentarioForm(request.POST)
        if form.is_valid():
         

            comentario = form.save(commit=False)
            comentario.usuario = request.user
           
            comentario.save()
            return redirect('/comentarios')
    filtro = request.GET.get('usuario')
    if filtro:
        comentarios = Comentario.objects.filter(usuario__username=filtro).order_by('-fecha')
    else:
        comentarios= Comentario.objects.all().order_by('-fecha')
    
    return render(request,'tareas/comentario.html', {'form':form,'comentarios':comentarios})

def lista_tareas(request):
    
    tareas = Tarea.objects.all()
    return render(request, "tareas/tareas.html",{"tareas": tareas})

def register(request):
    if request.method == 'POST':
         form = RegistroForm(request.POST)
         #form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/accounts/login/')

    else:
        form = RegistroForm()
    token = {}
            #token.update(csrf(request))
    token['form'] = form

    return render(request,'registration/registro.html',token)

def home(request):
    return redirect('/login/')

def editar_tareas(request):
    form= TareaForm()

    if request.method == "POST":

        form = TareaForm(request.POST)
        if form.is_valid():
         

            tarea = form.save(commit=False)
            tarea.usuario = request.user
           
            tarea.save()	
    return render(request, "tareas/editar_tareas.html",{"form": form})


     
