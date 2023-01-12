from django.contrib import admin
from django.urls import path
from django.urls import include
from AVENGER.views import *
from applogin.views import *
from appchecklists.views import *

urlpatterns = [
    path('', vista_login, name="AVENGER-login"),
]