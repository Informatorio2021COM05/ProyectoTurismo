from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def iniciar_s(request):
    siguiente = request.GET.get("next","http://127.0.0.1:8000/perfil_user/")
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect(siguiente)

    template = "perfilUser/usuario.html"
    contexto = {"form":form}
    return render(request, template, contexto)

def cerrar_s(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")

# Create your views here.
def perfil_user(request):
    return render(request, "ProyectoWebApp/home2.html",{})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.success(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request, 'perfilUser/register.html', context)
