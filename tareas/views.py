from django.shortcuts import render,redirect
from .models import Categoria,Comentario,Tarea
from .forms import Comentarios
from django.contrib.auth.decorators import login_required
# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()

@login_required
def comentario(request):
    form = Comentarios()
   

    if request.method == "POST":

        form = Comentarios(request.POST)
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



