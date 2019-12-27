from django.contrib import admin
from apps.transportista.models import Transportista


from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Transportista)

@admin.register(Transportista)
class ViewAdmin(ImportExportModelAdmin):
    pass
