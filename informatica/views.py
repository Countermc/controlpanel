from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'informatica/home.html', context)

def automatizacion(request):
    return render(request, 'informatica/automatizacion.html', {'title': 'Automatizacion'})

def tareas(request):
    return render(request, 'informatica/tareas.html', {'title': 'tareas'})

def calendario(request):
    return render(request, 'informatica/calendario.html', {'title': 'calendario'})

def login(request):
    return render(request, 'informatica/login.html', {'title': 'login'})

def incidencias(request):
    return render(request, 'informatica/incidencias.html', {'title': 'incidencias'})
