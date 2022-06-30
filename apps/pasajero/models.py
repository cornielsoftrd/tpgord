from django.db import models
from apps.ruta.models import Ruta
from apps.sites.models import Site


# Create your models here.


class Cuenta(models.Model):
    id_cuenta = models.IntegerField(primary_key=True)
    nombre_cuenta = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nombre_cuenta)


class Pasajero(models.Model):
    id_pasajero = models.IntegerField(primary_key=True)  # el codigo del empleado
    nombre = models.CharField(max_length=50,)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(unique=True, max_length=50, null=True)

    # ruta = models.ForeignKey(Ruta, verbose_name="Ruta Pasajero", on_delete=models.SET_DEFAULT, null=False, blank=False)
    Ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default=None)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class Horario(models.Model):
    pasajero=models.ForeignKey(Pasajero,on_delete=models.CASCADE,null=True,blank=True)
    dia=models.CharField(max_length=30,null=True,blank=True)
    hora_entrada = models.TimeField(null=True,blank=True)
    hora_salida = models.TimeField(null=True,blank=True)

    def __str__(self):
            return "%s" % (str(self.pasajero) + " :   " + str(self.pasajero.id_pasajero) + " :   " + str(self.dia))