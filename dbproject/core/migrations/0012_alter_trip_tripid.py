# Generated by Django 4.1.1 on 2023-12-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_organization_orgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='tripID',
            field=models.CharField(blank=True, max_length=500, primary_key=True, serialize=False),
        ),
    ]