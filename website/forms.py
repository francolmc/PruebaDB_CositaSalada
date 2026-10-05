from django import forms
from .models import Proyecto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ya existe una cuenta con ese correo.')
        return email
