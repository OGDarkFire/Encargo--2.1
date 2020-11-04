from django.contrib import admin
from gestionPaginas.models import Historial
from gestionPaginas.models import Invocador

# Register your models here.
class InvocadorAdmin(admin.ModelAdmin):
    list_display=("Usuario","Nivel","ChampMain")
    list_filter=("Nivel","ChampMain")


admin.site.register(Invocador, InvocadorAdmin)
admin.site.register(Historial)