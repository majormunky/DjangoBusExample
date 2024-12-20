# Generated by Django 5.1.2 on 2024-10-25 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_bus_agency"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seatuserlink",
            name="date_of_departure",
        ),
        migrations.CreateModel(
            name="BusTrip",
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
                ("departure_time", models.DateTimeField()),
                (
                    "bus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.bus"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="seatuserlink",
            name="departure_time",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.bustrip",
            ),
            preserve_default=False,
        ),
    ]
