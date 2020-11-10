"""EncargoPagina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login
from gestionPaginas import views


urlpatterns = [
    path('admin/', admin.site.urls,name="Admin"),
        # localhost:8000/
    path('pagina1/', views.pagina1, name="Pagina1"),
    path('pagina2/', views.pagina2, name="Pagina2"),
    path('pagina3/', views.pagina3, name="Pagina3") ,
    path('buscarinvocador/', views.buscarinvocador, name="buscarinvocador"),
    path('buscar/', views.buscar),
    path('login/', views.login, name="Login"),
]

#Nicolas -- nicolas02  (Superusuario)
#Brian -- nicolas02    (usuario) --agregar,actualizar,ver --Historial,Invocador
#Maxi -- nicolas02     (usuario) -Borrar, ver --Invocador
#Alvarez -- nicolas02  (usuario) -- Solo vista --Historial,Invocador
