# Generated by Django 4.2 on 2023-05-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0012_alter_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='text',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
