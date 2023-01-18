from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appchecklists.models import Checklist

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
        check = Checklist(
            request.POST["satelite"],
            request.POST["orbita"],
            request.POST["exitoso"],
            request.POST["incidente"],
            request.POST["comentario"],
            request.POST["_01chk"],request.POST["_02chk"],request.POST["_03chk"],
            request.POST["_04chk"],request.POST["_05chk"],request.POST["_06chk"],
            request.POST["_07chk"],request.POST["_08chk"],request.POST["_09chk"],
            request.POST["_10chk"],request.POST["_11chk"],)
        check.save()
        return render(request, "check_guardar.html")
    return render(request, "list.html")