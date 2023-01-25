from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def vista_mensajes(request):
    return render(request, "mensajes.html")

# Create your views here.
