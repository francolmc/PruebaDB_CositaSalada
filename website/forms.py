from django import forms
from .models import Proyecto

# Crearemos el formulario para la gestion de proyectos
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo',
            'descripcion',
            'categoria',
            'tecnologias',
            'etiquetas'
        ]