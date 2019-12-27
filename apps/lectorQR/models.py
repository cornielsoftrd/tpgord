from django.db import models

# Create your models here.
class LectorQr(models.Model):
    datos_codigo = models.CharField(max_length=50)
