from django.urls import path
from appmensajes.views import *

urlpatterns = [
    path('mensajes/', vista_mensajes, name="mensajes"),
    path('mensajes/create', MensajeCrear.as_view(), name="mensaje-create"),
    path('mensajes/list', MensajeList.as_view(), name="mensaje-list"),
]