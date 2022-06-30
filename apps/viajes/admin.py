from django.contrib import admin
from apps.viajes.models import Viaje, ViajeAdministrativo,Excepciones

from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Viaje)
#admin.site.register(ViajeAdministrativo)

@admin.register(Viaje, ViajeAdministrativo,Excepciones)
class ViewAdmin(ImportExportModelAdmin):
    pass