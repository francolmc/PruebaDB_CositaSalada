from django.shortcuts import render, redirect
from .forms import ProyectoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', { 'form': form })