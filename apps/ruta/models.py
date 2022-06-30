from django.db import models

# Create your models here.
class Tipo_ruta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nombre)

class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    nombre_ruta = models.CharField(max_length=50)
    tipo_ruta=models.ManyToManyField(Tipo_ruta,null=True,blank=True)
    precio_ruta=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return "%s" % (self.nombre_ruta)


