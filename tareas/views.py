from django.shortcuts import render,redirect, get_object_or_404
from .models import Categoria,Comentario,Tarea
from .forms import ComentarioForm, TareaForm, Tarea_estado
from django.contrib.auth.decorators import login_required

# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()

@login_required
def comentario(request,id):
    form = ComentarioForm()
    tarea=get_object_or_404(Tarea, id=id)
    form_estado= Tarea_estado(instance=tarea)
    estado_viejo = tarea.estado 
    if request.method == "POST":
        if 'submit_estado' in request.POST:
            form_estado = Tarea_estado(request.POST, instance=tarea)
            if form_estado.is_valid():
                print(estado_viejo)
                form_estado.save()
                estado_nuevo = tarea.estado
                print(estado_nuevo)
                if estado_viejo != estado_nuevo:
                    usuario = request.user
                    texto = "{} cambiò el estado de {} a {}".format(usuario, estado_viejo, estado_nuevo)
                    Comentario(usuario=usuario,texto=texto, tarea=tarea, manual=False).save()

                return redirect(tarea)
        else:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user
                comentario.tarea = tarea
               
                comentario.save()
                return redirect(tarea)
    filtro = request.GET.get('usuario')
    if filtro:
        comentarios = Comentario.objects.filter(tarea=tarea, usuario__username=filtro).order_by('-fecha')
    else:
        comentarios= Comentario.objects.filter(tarea=tarea).order_by('-fecha')
    
    return render(request,'tareas/comentario.html', {'form':form,'form_estado':form_estado, 'comentarios':comentarios, 'tarea':tarea})

@login_required
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
            return redirect(tarea)
    return render(request, "tareas/editar_tareas.html",{"form": form})

     
