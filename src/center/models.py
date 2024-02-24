from django.db import models
from vaccine.models import Vaccine


# Create your models here.
class Center(models.Model):
    """Model definition for Center."""

    name = models.CharField(verbose_name="Center name", max_length=150)
    address = models.TextField(verbose_name="Center address", max_length=500)

    class Meta:
        """Meta definition for Center."""

        verbose_name = "Center"
        verbose_name_plural = "Centers"

    def __str__(self):
        """Unicode representation of Center."""
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.name}>"

    def get_absolute_url(self):
        """Return absolute url for Center."""
        return ""

    # TODO: Define custom methods here


class Storage(models.Model):
    """Model definition for Storage."""

    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name="storage")
    vaccine = models.ForeignKey(
        Vaccine, on_delete=models.CASCADE, related_name="storage"
    )
    total_quantity = models.IntegerField(verbose_name="Total quantity", default=0)
    booked_quantity = models.IntegerField(verbose_name="Booked quantity", default=0)

    class Meta:
        """Meta definition for Storage."""

        verbose_name = "Storage"
        verbose_name_plural = "Storages"

    def __str__(self):
        """Unicode representation of Storage."""
        return f"{self.center.name} - {self.vaccine.name}"

    # string representation of the object for terminal
    def __repr__(self):
        return f"<{self.center.name} - {self.vaccine.name}>"

    def get_absolute_url(self):
        """Return absolute url for Storage."""
        return ""

    # TODO: Define custom methods here
