from django.db import models
from apps.ruta.models import Ruta
from apps.vendor.models import Vendor


# Create your models here.
class Transportista(models.Model):
    codigo_transportista = models.CharField(max_length=50,
        primary_key=True
    )  # la cedula del transportista
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ruta = models.ManyToManyField(Ruta)
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)
