# Generated by Django 4.0.1 on 2022-01-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='fips',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='country',
            name='iso3',
            field=models.CharField(max_length=30),
        ),
    ]
