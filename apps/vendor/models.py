from django.db import models

# Create your models here.
class Vendor(models.Model):
    id_vendor = models.IntegerField(
        primary_key=True
    )  # la cedula del transportista
    nombre_vendor = models.CharField(max_length=50)
    nombre_vendor = models.CharField(max_length=50)


    def __str__(self):
        return "%s" % (self.nombre_vendor)