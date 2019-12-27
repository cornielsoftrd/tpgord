from django.db import models
from datetime import datetime
from apps.vendor.models import Vendor

# Create your models here.


class Viaje(models.Model):

    id_viaje = models.AutoField(primary_key=True)
    numero_viaje = models.CharField(max_length=1024, default="00000000")
    transportista = models.CharField(max_length=50)
    fecha_viaje = models.DateField()
    hora_viaje = models.TimeField()
    tipo_viaje = models.CharField(max_length=30, default="sin asignar")
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    id_pasajero = models.CharField(max_length=50)
    nombre_pasajero = models.CharField(max_length=50)
    apellido_pasajero = models.CharField(max_length=50)
    campaña_pasajero = models.CharField(max_length=50)
    site_pasajero = models.CharField(max_length=50)
    ruta_pasajero = models.CharField(max_length=50)
    direccion_pasajero = models.CharField(max_length=50)

    # estos dos ultimos campos se ulizaran al momento de agregar al los pasajeros de modo manual cuando esten fuera de su horario o por cualquier otra razon
    # si el pasajero se agrega de manera manual, el transportista debera poner la razon de la excepcion y la excepcion se cambiara a True para luego poder filtrar los pasajeros con excepciones
    excepcion = models.BooleanField(default=False)
    razon_excepcion = models.TextField(default="Sin Espesificar")

    def __str__(self):
        return "%s" % (self.transportista)

class ViajeAdministrativo(models.Model):
    
   
    numero_viaje = models.CharField(primary_key=True, max_length=100)
    usuario = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, default="vacio") #esta llave Foranea dice q un viaje admisnistrativo es realizado por un vendor
    fecha_viaje = models.DateField()
    hora_viaje = models.TimeField()
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    tipo_vehiculo = models.CharField(max_length=30)
    tipo_visita = models.CharField(max_length=30)
    numero_contacto = models.CharField(max_length=30)
    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=30, default="Pendiente")

    def __str__(self):
        return "%s" % (self.usuario)
