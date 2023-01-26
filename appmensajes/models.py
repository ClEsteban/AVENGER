from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    operador=models.CharField(max_length=50, default=False)
    mensaje = models.TextField(verbose_name= 'Mensaje', null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        fila = f"Mensaje: {self.mensaje} - Remitente: {self.operador}"
        return fila
