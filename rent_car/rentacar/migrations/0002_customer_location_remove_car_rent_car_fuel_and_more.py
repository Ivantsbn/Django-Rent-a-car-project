# Generated by Django 4.2 on 2023-04-30 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='rent',
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(default='petrol', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rentacar.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rentacar.customer')),
            ],
        ),
    ]