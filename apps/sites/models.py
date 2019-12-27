from django.db import models

# Create your models here.


class Site(models.Model):
    id_site = models.IntegerField(primary_key=True)
    nombre_site = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre_site
