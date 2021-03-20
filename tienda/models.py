from django.db import models

# Create your models here.

class Ciudades(models.Model):
    # codigo_postal=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    zona_turistica=models.BooleanField(primary_key=False)
    codigo_postal=models.IntegerField()
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    creacion=models.DateTimeField(auto_now_add=True)
    actualizacion=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="ciudad"
        verbose_name_plural="ciudades"

    def __str__(self):
        return self.ciudad


class AtractivosTuristicos(models.Model):
    nombre=models.CharField(max_length=50)
    ciudad_origen=models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    horarios=models.CharField(max_length=50)
    precio_entrada=models.FloatField()
    creacion=models.DateTimeField(auto_now_add=True)
    actualizacion=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="AtractivoTuristico"
        verbose_name_plural="AtractivosTuristicos"

    def __str__(self):
        tex = '{0}-{1}-{2}-{3}-{4}-{5}-{6}'
        return tex.format(self.nombre, self.ciudad_origen, self.imagen, self.horarios, self.precio_entrada, self.creacion, self.actualizacion)
        
