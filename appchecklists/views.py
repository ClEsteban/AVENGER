from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appchecklists.models import Checklist
from appchecklists.forms import PasadaFormulario

@login_required
def vista_lista(request):
    return render(request, "list.html")

@login_required
def vista_sarsubmenu(request):
    return render(request, "SARsubmenu.html")

@login_required
def vista_ssarsubmenu(request):
    return render(request, "SSARsubmenu.html")

@login_required
def vista_saocom1amenu(request):
    return render(request, "SAOCOM1Amenu.html")

@login_required
def vista_saocom1bmenu(request):
    return render(request, "SAOCOM1Bmenu.html")

@login_required
def vista_metopb(request):
    context ={}
    context['form']= PasadaFormulario()
    return render(request, "checklists/255 METOPB.html", context)

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

@login_required
def vista_sarx(request):
    return render(request, "checklists/SARX13D.html")

@login_required
def vista_sars(request):
    return render(request, "checklists/SARTTC13D.html")

@login_required
def vista_ssarx(request):
    return render(request, "checklists/SSARX13D.html")

@login_required
def vista_ssars(request):
    return render(request, "checklists/SSARTTC13D.html")

@login_required
def vista_saocom1aetc(request):
    return render(request, "checklists/410 SAOCOM1A.html")

@login_required
def vista_saocom1betc(request):
    return render(request, "checklists/411 SAOCOM1B.html")

@login_required
def vista_saocom1aett(request):
    return render(request, "checklists/SAOCOM1AETT.html")

@login_required
def vista_saocom1bett(request):
    return render(request, "checklists/SAOCOM1BETT.html")

@login_required
def vista_guardar_check(request):
    if request.method == 'POST':
        formulario = PasadaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data            
            check = Checklist(
            satelite=informacion["satelite"],
            orbita=informacion["orbita"],
            exitoso=informacion["exitoso"],
            incidente=informacion["incidente"],
            comentario=informacion["comentario"],
            a01ckb=informacion["a01ckb"],
            a02ckb=informacion["a02ckb"],
            a03ckb=informacion["a03ckb"],
            a04ckb=informacion["a04ckb"],
            a05ckb=informacion["a05ckb"],
            a06ckb=informacion["a06ckb"],
            a07ckb=informacion["a07ckb"],
            a08ckb=informacion["a08ckb"],
            a09ckb=informacion["a09ckb"],
            a10ckb=informacion["a10ckb"],
            a11ckb=informacion["a11ckb"],           
            )
            check.save()
            return render(request, "check_guardar.html")
    else:
        formulario = PasadaFormulario()
    return render(request, "check_guardar.html", {"formulario":formulario})