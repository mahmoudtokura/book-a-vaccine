from django.db import models
from django.contrib.auth import get_user_model
from center.models import Center
from vaccine.models import Vaccine

User = get_user_model()


# Create your models here.
class Campaign(models.Model):
    """Model definition for Campaign."""

    center = models.ForeignKey(
        Center, on_delete=models.CASCADE, related_name="campaigns"
    )
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    agents = models.ManyToManyField(User, blank=True, related_name="campaigns")

    class Meta:
        """Meta definition for Campaign."""

        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        """Unicode representation of Campaign."""
        return f"{self.vaccine.name.upper()} - {self.center.name.upper()}"

    def get_absolute_url(self):
        """Return absolute url for Campaign."""
        return ""

    # TODO: Define custom methods here


class Slot(models.Model):
    """Model definition for Slot."""

    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="slots"
    )
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    max_capacity = models.PositiveIntegerField(default=1, null=True, blank=True)
    reserved = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        """Meta definition for Slot."""

        verbose_name = "Slot"
        verbose_name_plural = "Slots"

    def __str__(self):
        """Unicode representation of Slot."""
        return f"{self.date} - {self.start_time} to {self.end_time}"
