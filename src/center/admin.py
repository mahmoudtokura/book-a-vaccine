from django.contrib import admin

from .models import Center, Storage


# Register your models here.
class CenterAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "address",
                )
            },
        ),
    )


class StorageAdmin(admin.ModelAdmin):
    list_display = ("center", "vaccine", "total_quantity", "booked_quantity")
    search_fields = ("center__name", "vaccine__name")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "center",
                    "vaccine",
                    "total_quantity",
                    "booked_quantity",
                )
            },
        ),
    )


admin.site.register(Center, CenterAdmin)
admin.site.register(Storage, StorageAdmin)
