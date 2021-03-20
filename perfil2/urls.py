from django.urls import path
from .views import register

app_name = "perfil2"
urlpatterns = [
	
    path('register/', register, name='register'),
]
