# Generated by Django 2.2.10 on 2020-11-23 14:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0020_habitaciones_tele'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comnombre', models.CharField(max_length=100)),
                ('ciunombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
            },
        ),
        migrations.CreateModel(
            name='ProductosDeptos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnombre', models.CharField(blank=True, max_length=20, null=True)),
                ('pdescripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('pvalor', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.AlterModelOptions(
            name='tipo_pension',
            options={'verbose_name': 'Tipo de Pension', 'verbose_name_plural': 'Tipos de Pensiones'},
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='baños',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='camas',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='capacidad',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='garaje',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='image',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='num_habitacion',
        ),
        migrations.RemoveField(
            model_name='habitaciones',
            name='tele',
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='depdir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='depfechacompra',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='depnum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='depnumdep',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='depprecio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='habitaciones',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='reservas_habitacion',
            name='status_payment',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('Pendiente', 'Pendiente'), ('Error', 'Error'), ('Cancelado', 'Cancelado'), ('Activa', 'Activa'), ('Finalizada', 'Finalizada')], default='Pendiente', max_length=100),
        ),
        migrations.AlterField(
            model_name='tipo_alojamiento',
            name='descripcion',
            field=models.CharField(choices=[('Doble', 'Doble'), ('Individual', 'Individual')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tipo_pension',
            name='tipo_pension',
            field=models.CharField(choices=[('Completa', 'Completa'), ('Media', 'Media'), ('Desayuno', 'Desayuno'), ('Nada', 'Nada')], max_length=50),
        ),
        migrations.CreateModel(
            name='DetalleDepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qprod', models.IntegerField(default=0)),
                ('iddepto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.Habitaciones')),
                ('idproductos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.ProductosDeptos')),
            ],
            options={
                'verbose_name': 'Detalle Departamento',
                'verbose_name_plural': 'Detalle Departamentos',
            },
        ),
        migrations.AddField(
            model_name='habitaciones',
            name='idcomuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.Comuna'),
        ),
    ]
