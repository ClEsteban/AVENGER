from django.urls import path
from AVENGER.views import *
from applogin.views import *
from appchecklists.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', vista_lista, name="avenger-lista"),
    path('255METOPB/', vista_metopb, name="metopb"),
    path('255METOPB/', vista_metopc, name="metopc"),
    path('345AQUA/', vista_aqua, name="aqua"),
    path('345TERRA/', vista_terra, name="terra"),
    path('792LANDSAT8/', vista_landsat8, name="landsat8"),
    path('715 SPOT6/', vista_spot6, name="spot6"),
    path('425 SPOT7/', vista_spot7, name="spot7"),
]