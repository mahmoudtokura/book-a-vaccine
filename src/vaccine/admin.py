from django.contrib import admin

from .models import Vaccine


# Register your models here.
class VaccineAdmin(admin.ModelAdmin):
    list_display = ("name", "number_of_doses", "minimum_age")
    search_fields = ("name", "description")
    list_filter = ("number_of_doses", "minimum_age")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "number_of_doses",
                    "interval",
                    "storage_temperature",
                    "minimum_age",
                )
            },
        ),
    )


admin.site.register(Vaccine, VaccineAdmin)
