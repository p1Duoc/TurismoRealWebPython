# Generated by Django 3.0.3 on 2020-02-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrousuario',
            name='password2',
        ),
        migrations.AlterField(
            model_name='registrousuario',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
