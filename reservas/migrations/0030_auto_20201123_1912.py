# Generated by Django 2.2.10 on 2020-11-23 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0029_auto_20201123_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productosdeptos',
            old_name='pdescripcion',
            new_name='Descripción',
        ),
        migrations.RenameField(
            model_name='productosdeptos',
            old_name='pnombre',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='productosdeptos',
            old_name='pvalor',
            new_name='Valor',
        ),
    ]