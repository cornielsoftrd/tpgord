from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import Account

# Register your models here.
# admin.site.register(Account)


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "phone",
        "date_joined",
        "last_login",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_transportista",
    )

    search_fields = (
        "email",
        "username",
    )

    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
