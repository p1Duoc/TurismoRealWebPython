# Generated by Django 2.2.10 on 2020-11-23 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0028_auto_20201123_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comuna',
            old_name='Cuidad',
            new_name='Ciudad',
        ),
    ]