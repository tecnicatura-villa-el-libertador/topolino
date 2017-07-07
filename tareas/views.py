from django.shortcuts import render,redirect
from .models import Categoria,Comentario
from .forms import Comentarios

# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()


def comentario(request):
    form = Comentarios()
   

    if request.method == "POST":

        form = Comentarios(request.POST)
        if form.is_valid():
         

            comentario = form.save(commit=False)
           
           
            comentario.save()
            return redirect('/comentarios')
    filtro = request.GET.get('nombre')
    if filtro:
        comentarios = Comentario.objects.filter(nombre=filtro).order_by('-fecha')
    else:
        comentarios= Comentario.objects.all().order_by('-fecha')
    
    return render(request,'tareas/comentario.html', {'form':form,'comentarios':comentarios})
