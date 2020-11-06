from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from gestionPaginas.models import Invocador

# Create your views here.

def pagina1(request):
    return render(request, "PaginaLOL.html")

def pagina2(request):
    return render(request, "PaginaLOL2.html")

def pagina3(request):
    return render(request, "PaginaLOL3.html")

def buscarinvocador (request):

    return render(request, "BuscarInvocador.html")

def buscar(request):

    if request.GET["prd"]:

        Usuarios=request.GET["prd"]

        Invocadors=Invocador.objects.filter(nombre_icontains=Usuarios)

        return render(request,"BuscarInvocador.html", {"invocador": Invocadors, "query": Usuarios})
    
    else:
        mensaje="Debe ingresar un usuario"
    

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "PaginaLOL.html")
    # En otro caso redireccionamos al login
    return redirect('/login')   

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})