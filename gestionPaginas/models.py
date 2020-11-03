from django.db import models

# Create your models here.

class Invocador(models.Model):
    Usuario=models.CharField(max_length=30)
    Nivel=models.IntegerField()
    ChampMain=models.CharField(max_length=30)

class Historial(models.Model):
    Campeon=models.CharField(max_length=20)
    Duracion=models.DateTimeField()
    kills=models.IntegerField()
    deaths=models.IntegerField()
    assist=models.IntegerField()
