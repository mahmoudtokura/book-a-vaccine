from django.contrib import admin
from .models import Vaccination


# Register your models here.
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ("patent", "campaign", "slot", "date", "is_vaccinated")
    search_fields = (
        "patent__first_name",
        "patent__last_name",
        "campaign__vaccine__name",
    )
    list_filter = ("campaign__vaccine__name", "is_vaccinated")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "patent",
                    "campaign",
                    "slot",
                    "date",
                    "is_vaccinated",
                )
            },
        ),
    )


admin.site.register(Vaccination, VaccinationAdmin)
