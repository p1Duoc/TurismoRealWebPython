# Generated by Django 3.0.2 on 2020-03-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0009_auto_20200225_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitaciones',
            name='habitacion_hotel',
        ),
        migrations.RemoveField(
            model_name='precio_pension',
            name='hotel_tipo_pension',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
