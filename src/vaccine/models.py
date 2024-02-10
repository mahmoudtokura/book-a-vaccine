from django.db import models


# Create your models here.
class Vaccine(models.Model):
    """Model definition for Vaccine."""

    name = models.CharField(verbose_name="Vaccine name", max_length=50)
    description = models.TextField(verbose_name="Vaccine description", max_length=1024)
    number_of_doses = models.IntegerField(verbose_name="Number of doses", default=1)
    interval = models.IntegerField(
        verbose_name="Interval between doses",
        default=0,
        help_text="Provide interval in days",
    )
    storage_temperature = models.IntegerField(
        verbose_name="Storage temperature",
        help_text="Provide storage temperature in Celsius",
        null=True,
        blank=True,
    )
    minimum_age = models.IntegerField(
        verbose_name="Minimum age",
        help_text="Provide minimum age for vaccine",
        default=0,
    )

    class Meta:
        """Meta definition for Vaccine."""

        verbose_name = "Vaccine"
        verbose_name_plural = "Vaccines"

    def __str__(self):
        """Unicode representation of Vaccine."""
        return f"<Vaccine: {self.name}>"

    def get_absolute_url(self):
        """Return absolute url for Vaccine."""
        return ""

    # TODO: Define custom methods here
