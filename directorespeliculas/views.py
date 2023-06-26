from django.shortcuts import render
from .models import Genero,Pelicula,PeliculaInstance,Director

# Create your views here.
def index(request):
    cantidad_peliculas = Pelicula.objects.all().count()
    cantidad_generos = Genero.objects.all().count()
    cantidad_directores = Director.objects.all().count()
    cantidad_instancias = PeliculaInstance.objects.all().count()
    disponibilidad_peliculas = PeliculaInstance.objects.filter(status__exact='A').count()

    return render(
        request,
        'index.html',
        context={
            'cantidad_peliculas': cantidad_peliculas,
            'cantidad_generos': cantidad_generos,
            'cantidad_directores': cantidad_directores,
            'disponibilidad_peliculas': disponibilidad_peliculas,
            'cantidad_instancias': cantidad_instancias
        }
    ) 

