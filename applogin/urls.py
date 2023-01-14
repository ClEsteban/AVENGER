from django.contrib import admin
from django.urls import path
from django.urls import include
from AVENGER.views import *
from applogin.views import *
from appchecklists.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('applogin/', vista_login, name="AVENGER-login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="AVENGER-logout"),
]