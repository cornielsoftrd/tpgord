from django.db import models

# Create your models here.


class Ruta(models.Model):
    id_ruta = models.AutoField(primary_key=True)
    nombre_ruta = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nombre_ruta)
