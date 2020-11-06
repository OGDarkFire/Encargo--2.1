from django.contrib import admin
from gestionPaginas.models import Historial
from gestionPaginas.models import Invocador

# Register your models here.

class InvocadorAdmin(admin.ModelAdmin):
    list_display=("Usuario","Nivel","ChampMain") #como se muestra la Informacion que se muestra en la pagina Admin
    list_filter=("Nivel","ChampMain")#Filtros de la pagina

class HistorialAdmin(admin.ModelAdmin):
    list_display=("Campeon","Duracion","Kills", "Deaths","Assist" )#Como se muestra la informacion en la pagina Admin
    list_filter=("Campeon","Duracion")#Filtros de la pagina


admin.site.register(Invocador, InvocadorAdmin)
admin.site.register(Historial)