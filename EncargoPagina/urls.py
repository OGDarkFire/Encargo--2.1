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
from gestionPaginas import views

urlpatterns = [
    path('admin/', admin.site.urls),
        # localhost:8000/
    path('pagina1/', views.pagina1, name="Pagina1"),
    path('pagina2/', views.pagina2, name="Pagina2"),
    path('pagina3/', views.pagina3, name="Pagina3") ,
    path('pagina31/', views.pagina31, name="Pagina31") ,
    path('pagina32/', views.pagina32, name="Pagina32") ,
    path('pagina33/', views.pagina33, name="Pagina33") ,
    path('pagina34/', views.pagina34, name="Pagina34") ,
    path('login/', views.login, name="Login")
]
