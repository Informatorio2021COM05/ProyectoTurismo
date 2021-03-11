from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def iniciar_sesion(request):
    siguiente = request.GET.get("next","http://127.0.0.1:8000/admin/")
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

    template = "perfil/login.html"
    contexto = {"form":form}
    return render(request, template, contexto)

def cerrar_sesion(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")