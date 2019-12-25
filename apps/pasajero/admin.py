from django.contrib import admin
from apps.pasajero.models import Pasajero, Cuenta
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(Pasajero)
#admin.site.register(Cuenta)

@admin.register(Pasajero,Cuenta)
class ViewAdmin(ImportExportModelAdmin):
    pass