from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm, RegistroForm
from .models import Proyecto
from django.contrib.auth import login
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def proyectos_home(request):
    # proyectos = Proyecto.objects.all()
    # return render(request, 'home_proyectos.html', {'proyectos': proyectos})
    q = request.GET.get('q', '')
    proyectos = Proyecto.objects.filter(usuario = request.user)
    if q:
        proyectos = proyectos.filter(titulo__icontains=q)
    proyectos = proyectos.order_by('titulo')
    return render(request, 'home_proyectos.html', {'proyectos': proyectos, 'q': q})


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            form.save_m2m()
            messages.success(request, 'Proyecto creado.')
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', { 'form': form })

@login_required
def editar_proyecto(request, pk):
    # Buscar el proyecto
    proyecto = get_object_or_404(Proyecto, pk = pk)

    if proyecto.usuario != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'crear_proyecto.html', {'form': form})

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if proyecto.usuario != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'confirmar_eliminar.html', {'proyecto': proyecto})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenido. {user.username}. Tu cuenta fue creada.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})