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
    _01ckb = models.BooleanField()
    _02ckb = models.BooleanField()
    _03ckb = models.BooleanField()
    _04ckb = models.BooleanField()
    _05ckb = models.BooleanField()
    _06ckb = models.BooleanField()
    _07ckb = models.BooleanField()
    _08ckb = models.BooleanField()
    _09ckb = models.BooleanField()
    _10ckb = models.BooleanField()
    _11ckb = models.BooleanField()
    _12ckb = models.BooleanField()
    _13ckb = models.BooleanField()
    _14ckb = models.BooleanField()
    _15ckb = models.BooleanField()
    _16ckb = models.BooleanField()
    _17ckb = models.BooleanField()
    _18ckb = models.BooleanField()
    _19ckb = models.BooleanField()
    _20ckb = models.BooleanField()
    _21ckb = models.BooleanField()
    _22ckb = models.BooleanField()
    _23ckb = models.BooleanField()
    _24ckb = models.BooleanField()
    _25ckb = models.BooleanField()



    
