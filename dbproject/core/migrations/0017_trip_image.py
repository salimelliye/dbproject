# Generated by Django 4.1.1 on 2023-12-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_vehicle_platenb'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
