# Generated by Django 2.2.10 on 2020-11-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0036_auto_20201128_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_alojamiento',
            name='precio',
            field=models.DecimalField(choices=[(20.0, 20.0), (10.0, 10.0), (30.0, 30.0), (40.0, 40.0), (50.0, 50.0), (60.0, 60.0), (70.0, 70.0), (80.0, 80.0), (90.0, 90.0)], decimal_places=2, max_digits=5),
        ),
    ]
