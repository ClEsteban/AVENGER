from django.urls import path
from appmensajes.views import *

urlpatterns = [
    path('mensajes/', vista_mensajes, name="mensajes"),
]