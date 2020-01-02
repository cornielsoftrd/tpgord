from django.db import models

# Create your models here.
class Vendor(models.Model):
    id_vendor = models.IntegerField(
        primary_key=True
    )  # la cedula del transportista
    nombre_vendor = models.CharField(max_length=50, unique=True)
    email_vendor = models.EmailField(max_length=100,blank=True,null=True, unique=True)
    telefono_vendor = models.CharField(max_length=50, unique=True, blank=True, null=True)
    


    def __str__(self):
        return "%s" % (self.nombre_vendor)

