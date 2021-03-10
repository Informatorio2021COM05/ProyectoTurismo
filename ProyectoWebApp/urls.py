from django.urls import path

from ProyectoWebApp.views import home, buscar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="Inicio"),
    path('buscar/', buscar, name="Busqueda"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)