from django.contrib import admin
from apps.sites.models import Site


from import_export.admin import ImportExportModelAdmin


# Register your models here.

#admin.site.register(Site)

@admin.register(Site)
class ViewAdmin(ImportExportModelAdmin):
    pass


