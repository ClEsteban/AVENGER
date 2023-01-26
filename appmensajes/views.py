from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from appmensajes.models import Mensaje


@login_required
def vista_mensajes(request):
    return render(request, "mensajes.html")

class MensajeCrear(CreateView):
   model = Mensaje
   success_url = "/mensajes"
   fields = ["mensaje"]

class MensajeList(ListView):
    model = Mensaje
    template_name = "mensajes.html"

# Create your views here.
