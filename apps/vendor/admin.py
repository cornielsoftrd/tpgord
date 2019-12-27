from django.contrib import admin
from apps.vendor.models import Vendor

from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Vendor)

@admin.register(Vendor)
class ViewAdmin(ImportExportModelAdmin):
    pass