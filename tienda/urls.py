from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tienda/', tienda, name="Tienda"),
    path('buscar2/', buscar, name="Buscar"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)