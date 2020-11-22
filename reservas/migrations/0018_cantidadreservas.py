# Generated by Django 3.0.2 on 2020-03-31 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0017_habitaciones_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadReservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite', models.IntegerField(default=10, verbose_name='limite')),
                ('reserva_habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Habitaciones')),
            ],
        ),
    ]
