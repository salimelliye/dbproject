# Generated by Django 4.2.7 on 2023-12-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0015_trip_orgid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="plateNb",
            field=models.CharField(
                blank=True, max_length=500, primary_key=True, serialize=False
            ),
        ),
    ]
