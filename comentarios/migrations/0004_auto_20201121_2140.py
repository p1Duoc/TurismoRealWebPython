# Generated by Django 3.1.3 on 2020-11-22 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_auto_20200315_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario_aprobado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
