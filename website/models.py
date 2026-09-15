from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Etiquetas, que funcione con un sistema de tags para poder buscar el proyecto
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    # tecnologia = models.CharField(max_length=100)
    # removemos el campo tecnologia y lo reemplazaremos por una 
    # relacion con la tabla Categoria
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='proyectos',
        null=True,
        blank=True
    )
    tecnologias = models.ManyToManyField(Tecnologia, related_name='proyectos', blank=True)
    etiquetas = models.ManyToManyField(
        Etiqueta,
        related_name='proyectos',
        blank=True
    )

    def __str__(self):
        return self.titulo
