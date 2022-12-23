from django.db import models

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    specialization = models.CharField(max_length=200, verbose_name='Profesion')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='chefs')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de Edicion')

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'
        ordering = ['-created']

    def __str__(self):
        return self.name