from django.db import models

# Create your models here.
# Aqui se ponen los modelos de la base de datos

class Invocador(models.Model):
    Usuario=models.CharField(max_length=30)
    Nivel=models.IntegerField()
    ChampMain=models.CharField(max_length=30)
    #Modelo invocador de la base de datos


    def __str__(self):
        return self.Usuario

class Historial(models.Model):
    Campeon=models.CharField(max_length=20)
    Duracion=models.DateTimeField()
    kills=models.IntegerField()
    deaths=models.IntegerField()
    assist=models.IntegerField()
    #Modelo historial de la base de datos
    def __str__(self):
        return self.Campeon
