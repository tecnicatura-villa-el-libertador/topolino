from django.shortcuts import render,redirect, get_object_or_404
from .models import Categoria,Comentario,Tarea
from .forms import ComentarioForm, TareaForm, Tarea_estado, BuscarForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def nombrecat(request):
    cat = Categoria.Object.all()

@login_required
def comentario(request,id):
    # instancio un formulario de comentario en blanco
    form = ComentarioForm()
    # trae un objeto tarea de cierto id
    tarea=get_object_or_404(Tarea, id=id)
    # formulario que permite cambiar estado de una tarea
    form_estado = Tarea_estado(instance=tarea)

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
    tareas = Tarea.objects.all()
    if request.method == "GET":
        if request.GET:
            form = BuscarForm(request.GET)
            if form.is_valid():
                tareas=tareas.filter(titulo__icontains=form.cleaned_data['buscar'])

    return render(request, "tareas/tareas.html",{"tareas": tareas,"form":form})

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

def editar_tareas(request,id = None):
    ''' 
	Esta vista sirve para crear un comentario nuevo en una tarea o modificar un comentario
    '''


    if id:
    	# si la tarea tiene un id me trae esa tarea sino da error 404
      	tarea = get_object_or_404(Tarea, id=id)
      	descripcion_vieja = tarea.descripcion
    else:
    	tarea = None

    # instancio un objeto que permite modificar 'titulo', 'descripcion', 'categoria', 'prioridad'
    form = TareaForm(instance = tarea)
    
    if request.method == "POST":
        form = TareaForm(request.POST, instance = tarea)
        print(request.POST)
        if form.is_valid():
        	tarea = form.save(commit=False)
        	tarea.usuario = request.user
        	tarea.save()
        	descripcion_nueva = tarea.descripcion

       		if descripcion_nueva != descripcion_vieja:
	        	usuario = request.user
	        	texto = "{} editó el comentario de {} a {}".format(usuario, descripcion_vieja, descripcion_nueva)
	        	Comentario(usuario = usuario,texto = texto, tarea = tarea, manual = False).save()

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

 