from django.contrib import admin
from apps.ruta.models import Ruta,Tipo_ruta
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Ruta)
@admin.register(Ruta)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Tipo_ruta)
class ViewAdmin(ImportExportModelAdmin):
    pass