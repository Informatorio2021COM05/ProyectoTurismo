from django.urls import path
from . import views
from .views import register

app_name = "perfil2"
urlpatterns = [
	
    path('register/', views.register, name='register'),
    path('register/perfil_form.html', views.register, name='registed'),
]
