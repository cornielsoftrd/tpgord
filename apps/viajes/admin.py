from django.contrib import admin
from apps.viajes.models import Viaje, ViajeAdministrativo

from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Viaje)
#admin.site.register(ViajeAdministrativo)

@admin.register(Viaje, ViajeAdministrativo)
class ViewAdmin(ImportExportModelAdmin):
    pass