from django.contrib import admin
from . models import Genero,Pelicula,PeliculaInstance,Director
# Register your models here.
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(PeliculaInstance)
admin.site.register(Director)
