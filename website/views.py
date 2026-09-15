from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

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