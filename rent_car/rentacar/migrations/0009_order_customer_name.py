# Generated by Django 4.2 on 2023-05-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0008_remove_order_customer_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
