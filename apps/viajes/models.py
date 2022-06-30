from django.db import models
from datetime import datetime
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
from apps.account.models import Account
from apps.ruta.models import Ruta
from apps.pasajero.models import Pasajero,Cuenta
from apps.sites.models import Site

# Create your models here.


class Viaje(models.Model):

    id_viaje = models.AutoField(primary_key=True)
    numero_viaje = models.CharField(max_length=1024, default="00000000")
    #transportista = models.CharField(max_length=50)
    transportista = models.ForeignKey(Account,null=True,blank=True, on_delete=models.CASCADE)
    site_destino_origen =models.CharField(max_length=50, blank=True, null=True)
    fecha_viaje = models.DateField()
    hora_viaje = models.TimeField()
    tipo_viaje = models.CharField(max_length=30, default="sin espesificar")
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    id_pasajero = models.ForeignKey(Pasajero,blank=False,null=True,on_delete=models.CASCADE)
    nombre_pasajero = models.CharField(max_length=50)
    apellido_pasajero = models.CharField(max_length=50)
    campaña_pasajero = models.ForeignKey(Cuenta,null=True,blank=False,on_delete=models.CASCADE)
    site_pasajero = models.ForeignKey(Site,null=True,blank=False,on_delete=models.CASCADE)
    #ruta_pasajero = models.CharField(max_length=50)
    ruta_pasajero = models.ForeignKey(Ruta,null=True,blank=True, on_delete=models.CASCADE)
    direccion_pasajero = models.CharField(max_length=100)

    # estos dos ultimos campos se ulizaran al momento de agregar al los pasajeros de modo manual cuando esten fuera de su horario o por cualquier otra razon
    # si el pasajero se agrega de manera manual, el transportista debera poner la razon de la excepcion y la excepcion se cambiara a True para luego poder filtrar los pasajeros con excepciones
    excepcion = models.BooleanField(default=False)
    razon_excepcion = models.TextField(default="Sin espesificar")

    def __str__(self):
        return "%s" % (str(self.transportista) + "( " +str(self.numero_viaje)+" )"+ "( " +str(self.fecha_viaje)+" )")

class ViajeAdministrativo(models.Model):
    
   
    numero_viaje = models.CharField(primary_key=True, max_length=100)
    usuario = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, default="Sin espesificar") #esta llave Foranea dice q un viaje admisnistrativo es realizado por un vendor
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

class Excepciones(models.Model):
    nombre_excepcion=models.CharField(max_length=50,null=False, blank=False)
    detalle_excepcion=models.TextField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return "%s" % (self.nombre_excepcion)