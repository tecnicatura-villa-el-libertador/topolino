from django.shortcuts import render,redirect, get_object_or_404
from .models import Categoria,Comentario,Tarea
from .forms import ComentarioForm, TareaForm, Tarea_estado, BuscarForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()

@login_required
def comentario(request,id):

    form = ComentarioForm()
    tarea=get_object_or_404(Tarea, id=id)
    form_estado= Tarea_estado(instance=tarea)
    tareas_asignado= tarea.asignado

    estado_viejo = tarea.estado 
    if request.method == "POST":
        if 'submit_estado' in request.POST:
           
            #import ipdb;ipdb.set_trace  
            form_estado = Tarea_estado(request.POST, instance=tarea)
             
            
            
            if form_estado.is_valid():
                print(estado_viejo)
                form_estado.save()
                estado_nuevo = tarea.estado
                print(estado_nuevo)
                if estado_viejo != estado_nuevo:
                    usuario = request.user
                    texto = "{} cambió el estado de {} a {}".format(usuario, estado_viejo, estado_nuevo)
                    Comentario(usuario=usuario,texto=texto, tarea=tarea, manual=False).save()
                    if estado_nuevo== tarea.EN_CURSO:
                       
                        tareas_asignado=usuario
                        tareas_asignado.save()
                        #import pdb;pdb.set_trace()
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
    form=BuscarForm()
    o = request.GET.get("o")
    s=request.GET.get("s")
    tareas = Tarea.objects.all()
    
    
    if s=="des":
        orden='-' + o
        s = "asc"
    else:
        orden = o
        s = "des"
    if orden:
        tareas = tareas.order_by(orden)
    if request.method == "GET":
        if request.GET:
            form = BuscarForm(request.GET)
            if form.is_valid():# "Q" sirve para hacer filtros de diferentes campos.
                q1=Q(titulo__icontains=form.cleaned_data['buscar'])
                q2=Q(descripcion__icontains=form.cleaned_data['buscar'])
                tareas=tareas.filter(q1|q2)

    return render(request, "tareas/tareas.html",{"tareas": tareas,"form":form,"s":s, 'o': o})

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

  
def buscar(request):
    form=BuscarForm()
    filtro = request.GET.get('titulo')
    if filtro:
        tareas = Tarea.objects.filter(tarea=tarea, titulo=filtro).order_by('-fecha')
    else:
        tareas= Tareas.objects.filter(tarea=tarea).order_by('-fecha')
    return render(request, "tareas/tareas.html",{"form": form})

