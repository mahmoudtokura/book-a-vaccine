# Generated by Django 5.0.1 on 2024-02-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vaccine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Vaccine name")),
                (
                    "description",
                    models.TextField(
                        max_length=1024, verbose_name="Vaccine description"
                    ),
                ),
                (
                    "number_of_doses",
                    models.IntegerField(default=1, verbose_name="Number of doses"),
                ),
                (
                    "interval",
                    models.IntegerField(
                        default=0,
                        help_text="Provide interval in days",
                        verbose_name="Interval between doses",
                    ),
                ),
                (
                    "storage_temperature",
                    models.IntegerField(
                        blank=True,
                        help_text="Provide storage temperature in Celsius",
                        null=True,
                        verbose_name="Storage temperature",
                    ),
                ),
                (
                    "minimum_age",
                    models.IntegerField(
                        default=0,
                        help_text="Provide minimum age for vaccine",
                        verbose_name="Minimum age",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vaccine",
                "verbose_name_plural": "Vaccines",
            },
        ),
    ]
