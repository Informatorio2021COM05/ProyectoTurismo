from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'Usuario {username} creado')
            
    else:
        form = UserRegisterForm()

        context = { 'form' : form }
        return render(request, 'perfil2/perfil_form.html/', context)

"""
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpView

    def form_valid(self, form):
        
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('http://127.0.0.1:8000/')
"""