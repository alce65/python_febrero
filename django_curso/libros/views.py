from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Libro

# Create your views here.

def libros(request):
    libros = Libro.objects.all()
    data = {'libros': libros}
    #data = dict(libros = libros)
    return render(request, 'libros.html', data )

def libro_detail(request, libro_id ):
    try:
       libro = Libro.objects.get(id = libro_id)
    except Libro.DoesNotExist:
        raise Http404('Ese libro no existe')
    data = dict(libro = libro)
    return render(request, 'libro.html', data )
    # return HttpResponse(f'<h1>Detalle del libro {libro_id}</h1>')
