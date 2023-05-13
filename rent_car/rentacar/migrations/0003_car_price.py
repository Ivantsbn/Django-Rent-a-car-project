# Generated by Django 4.2 on 2023-04-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0002_customer_location_remove_car_rent_car_fuel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=12),
            preserve_default=False,
        ),
    ]