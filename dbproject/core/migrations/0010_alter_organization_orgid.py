# Generated by Django 4.1.1 on 2023-12-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_trip_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='orgID',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]