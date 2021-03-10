from django.shortcuts import render, HttpResponse
from ServiciosApp.models import Servicio


# Create your views here.

def servicios(request):

	servicios=Servicio.objects.all()

	return render(request, "ServiciosApp/servicios.html", {"servicios": servicios})


