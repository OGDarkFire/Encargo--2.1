from django.shortcuts import render

# Create your views here.

def pagina1(request):
    return render(request, "PaginaLOL.html")

def pagina2(request):
    return render(request, "PaginaLOL2.html")

def pagina3(request):
    return render(request, "PaginaLOL3.html")