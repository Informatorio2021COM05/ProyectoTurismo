from django.contrib import admin
from tienda.models import Ciudades, AtractivosTuristicos
# Register your models here.

class CiudadesAdmin(admin.ModelAdmin):
	readonly_fields=('creacion', 'actualizacion')

class TuristicoAdmin(admin.ModelAdmin):
	readonly_fields=('creacion', 'actualizacion')


admin.site.register(Ciudades, CiudadesAdmin)
admin.site.register(AtractivosTuristicos, TuristicoAdmin)
