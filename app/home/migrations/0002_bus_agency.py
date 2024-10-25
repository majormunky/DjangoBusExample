# Generated by Django 5.1.2 on 2024-10-25 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bus",
            name="agency",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="home.agency"
            ),
            preserve_default=False,
        ),
    ]
