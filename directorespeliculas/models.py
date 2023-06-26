from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genero(models.Model):
    genero = models.CharField(max_length=64,help_text='Tipo de género')

    def __str__(self):
        return self.genero

class Pelicula(models.Model):
    title = models.CharField(max_length=32,help_text='Título del libro')
    director = models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)
    síntesis = models.TextField(max_length=150,help_text='Breve síntesis de la película')
    url = models.URLField(blank=True)
    isbn = models.CharField('ISBN', max_length=13,help_text='ISBN de 13 caracteres')
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('pelicula_detail',args=[str(self.id)])

class PeliculaInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='ID único para ésta película')
    pelicula = models.ForeignKey('Pelicula',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)

    LOAN_STATUS = (
        ('M','Maintenance'),
        ('O','On loan'),
        ('A','Available'),
        ('R','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='M',help_text='Disponibilidad de la película')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.pelicula.title}'


class Director(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    fecha_fallecimiento = models.DateField(null=True,blank=True)
    
    
    def get_absolute_url(self):
        return reverse('director-detail', args={'pk': self.pk})

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

