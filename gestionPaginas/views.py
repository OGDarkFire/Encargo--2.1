from django.shortcuts import render

# Create your views here.

def login(request):
    return render (request, "Login.html")

def pagina1(request):
    return render(request, "PaginaLOL.html")

def pagina2(request):
    return render(request, "PaginaLOL2.html")

def pagina3(request):
    return render(request, "PaginaLOL3.html")

def pagina31(request):
    return render (request, "PaginaLOL31.html")
    
def pagina32(request):
    return render (request, "PaginaLOL32.html")

def pagina33(request):
    return render (request, "PaginaLOL33.html")

def pagina34(request):
    return render (request, "PaginaLOL34.html")        