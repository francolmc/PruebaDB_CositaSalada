from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm
from .models import Proyecto

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def proyectos_home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'home_proyectos.html', {'proyectos': proyectos})

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', { 'form': form })

@login_required
def editar_proyecto(request, pk):
    # Buscar el proyecto
    proyecto = get_object_or_404(Proyecto, pk = pk)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'crear_proyecto.html', {'form': form})

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('home')
    return render(request, 'confirmar_eliminar.html', {'proyecto': proyecto})