from django.contrib import admin
from .models import Campaign, Slot


# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("center", "vaccine", "start_date", "end_date")
    search_fields = ("center__name", "vaccine__name")
    list_filter = ("start_date", "end_date")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "center",
                    "vaccine",
                    "start_date",
                    "end_date",
                    "agents",
                )
            },
        ),
    )


class SlotAdmin(admin.ModelAdmin):
    list_display = (
        "campaign",
        "date",
        "start_time",
        "end_time",
        "max_capacity",
        "reserved",
    )
    search_fields = ("campaign__center__name", "campaign__vaccine__name")
    list_filter = ("date", "start_time", "end_time")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "campaign",
                    "date",
                    "start_time",
                    "end_time",
                    "max_capacity",
                    "reserved",
                )
            },
        ),
    )


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Slot, SlotAdmin)
