# Generated by Django 5.0.1 on 2024-02-05 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("center", "0001_initial"),
        ("vaccine", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Storage",
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
                (
                    "total_quantity",
                    models.IntegerField(default=0, verbose_name="Total quantity"),
                ),
                (
                    "booked_quantity",
                    models.IntegerField(default=0, verbose_name="Booked quantity"),
                ),
                (
                    "center",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="storage",
                        to="center.center",
                    ),
                ),
                (
                    "vaccine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="storage",
                        to="vaccine.vaccine",
                    ),
                ),
            ],
            options={
                "verbose_name": "Storage",
                "verbose_name_plural": "Storages",
            },
        ),
    ]
