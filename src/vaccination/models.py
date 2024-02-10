from django.db import models
from django.contrib.auth import get_user_model
from campaign.models import Campaign, Slot

User = get_user_model()


# Create your models here.
class Vaccination(models.Model):
    """Model definition for Vaccination."""

    patent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vaccinations"
    )
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    is_vaccinated = models.BooleanField(default=False)
    update_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Vaccination."""

        verbose_name = "Vaccination"
        verbose_name_plural = "Vaccinations"

    def __str__(self):
        """Unicode representation of Vaccination."""
        return f"{self.patent.get_full_name()} - {self.slot} - {self.campaign.vaccine.name}"
