# myapp/views.py

# myapp/views.py

from django.shortcuts import render
from .models import Proyecto
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def index(request):
    return render(request, 'myapp/index.html')


def lista_proyectos(request):
    selected_tema = request.GET.get('tema')  # Obtener el tema seleccionado de la URL
    proyectos = Proyecto.objects.all()  # Obtener todos los proyectos por defecto

    if selected_tema:  # Si se ha seleccionado un tema
        proyectos = proyectos.filter(Tema=selected_tema)  # Filtrar los proyectos por el tema seleccionado

    return render(request, 'myapp/proyectos.html', {'proyectos': proyectos, 'selected_tema': selected_tema})

def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('nuevoproyecto')
        else:
            return render(request, 'myapp/login.html', {'error': 'Credenciales inválidas. Por favor, inténtalo de nuevo.'})
    else:
        return render(request, 'myapp/login.html')
