from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def vista_lista(request):
    return render(request, "list.html")

@login_required
def vista_metopb(request):
    return render(request, "checklists/255 METOPB.html")

@login_required
def vista_metopc(request):
    return render(request, "checklists/255 METOPC.html")

@login_required
def vista_aqua(request):
    return render(request, "checklists/345 AQUA.html")

@login_required
def vista_terra(request):
    return render(request, "checklists/341 TERRA.html")

@login_required
def vista_landsat8(request):
    return render(request, "checklists/792 LANDSAT8.html")

@login_required
def vista_spot6(request):
    return render(request, "checklists/715 SPOT6.html")

@login_required
def vista_spot7(request):
    return render(request, "checklists/425 SPOT7.html")