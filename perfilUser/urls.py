from django.urls import path
from . import views

app_name = "perfilUser"
urlpatterns = [
    path("perfil_user/", views.perfil_user, name="Usuario"),
    path("iniciar/", views.iniciar_s, name="iniciar"),
    path("cerrar/", views.cerrar_s, name="cerrar")
]
