from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Checklist(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    satelite = models.CharField(max_length=50)
    orbita = models.IntegerField()
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    incidente = models.IntegerField()
    comentario = models.TextField(max_length=250)
    exitoso = models.BooleanField()
    
