from django.urls import path

from ProyectoWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="Inicio"),
    path('buscar/', buscar, name="Busqueda"),
    path('perfil/', perfil, name="perfil"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)