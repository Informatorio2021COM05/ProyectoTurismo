from django.shortcuts import render, HttpResponse
from tienda.models import Ciudades, AtractivosTuristicos

# Create your views here.
def tienda(request):
	ciudades=Ciudades.objects.all()
	turistico=AtractivosTuristicos.objects.all()
	return render(request, "tienda/tienda.html", {"ciudades": ciudades, "turistico": turistico})


def buscar(request):

	if request.GET["prd"]:
		#mensaje = "Articulo buscado: %r" %request.GET["prd"]
		nombre_ingresado = request.GET["prd"]

		if len(nombre_ingresado) < 30:

			ciudades = AtractivosTuristicos.objects.filter(nombre__icontains=nombre_ingresado)  #este comando sirve para filtrar la base de datos

			return render(request, "tienda/buscar.html", {"ciudades": ciudades, "query": nombre_ingresado})
		else:

			mensaje = "El texto ingresado es demasiado extenso"

	else:
		mensaje = "No has introducido nada"

	return HttpResponse(mensaje)