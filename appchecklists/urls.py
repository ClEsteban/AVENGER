from django.urls import path
from AVENGER.views import *
from applogin.views import *
from appchecklists.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('lista/', vista_lista, name="avenger-lista"),
    path('sarmenu/', vista_sarsubmenu, name="sar-submenu"),
    path('ssarmenu/', vista_ssarsubmenu, name="ssar-submenu"),
    path('saocom1amenu/', vista_saocom1amenu, name="saocom1a-menu"),
    path('saocom1bmenu/', vista_saocom1bmenu, name="saocom1b-menu"),
    path('255METOPB/', vista_metopb, name="metopb"),
    path('255METOPC/', vista_metopc, name="metopc"),
    path('345AQUA/', vista_aqua, name="aqua"),
    path('345TERRA/', vista_terra, name="terra"),
    path('792LANDSAT8/', vista_landsat8, name="landsat8"),
    path('715 SPOT6/', vista_spot6, name="spot6"),
    path('425 SPOT7/', vista_spot7, name="spot7"),
    path('SARX/', vista_sarx, name="sarx"),
    path('SARS/', vista_sars, name="sars"),
    path('SSARX/', vista_ssarx, name="ssarx"),
    path('SSARS/', vista_ssars, name="ssars"),
    path('SAOCOM1AETC/', vista_saocom1aetc, name="saocom1aetc"),
    path('SAOCOM1BETC/', vista_saocom1betc, name="saocom1betc"),
    path('SAOCOM1AETT/', vista_saocom1aett, name="saocom1aett"),
    path('SAOCOM1BETT/', vista_saocom1bett, name="saocom1bett"),
    path('CHECKGUARDAR/', vista_guardar_check, name="checkguardar"),
]