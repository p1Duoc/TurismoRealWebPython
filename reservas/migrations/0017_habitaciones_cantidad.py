# Generated by Django 3.0.2 on 2020-03-31 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0016_reservas_habitacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitaciones',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
