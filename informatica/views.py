from django.shortcuts import render

posts = [
    {
        'author': 'Juan Moreno',
        'title': 'Problemas con el correo',
        'content': 'No puedo mandar correos ',
        'date_posted': 'Agosto 27, 2018'
    },
    {
        'author': 'Luis',
        'title': 'No funciona la impresora',
        'content': 'No puedo imprimir, llevo toda la mañana reiniciandola',
        'date_posted': 'Agosto 27, 2018'
    },
    {
        'author': 'Alberto',
        'title': 'BD hay que borrar un pvst',
        'content': 'No me deja borrar el pvst28004, podeis borrarlo vosotros?',
        'date_posted': 'Agosto 27, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
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
