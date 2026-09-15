from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto, Etiqueta

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    list_filter = ('categoria', 'tecnologias', 'etiquetas')
    search_fields = ('titulo', 'descripcion')

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Etiqueta)
admin.site.register(Proyecto, ProyectoAdmin)