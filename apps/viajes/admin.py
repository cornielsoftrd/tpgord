from django.contrib import admin
from apps.viajes.models import Viaje, ViajeAdministrativo

# Register your models here.

admin.site.register(Viaje )
admin.site.register(ViajeAdministrativo)