# Generated by Django 5.2 on 2025-04-09 12:45

import django.contrib.gis.db.models.fields
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogProduit",
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
                ("name", models.CharField(max_length=255)),
                ("ref", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                (
                    "geolocalization",
                    django.contrib.gis.db.models.fields.PointField(
                        geography=True, srid=4326
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "vector_search",
                    django.contrib.postgres.search.SearchVectorField(
                        verbose_name=["name", "description"]
                    ),
                ),
            ],
        ),
    ]
