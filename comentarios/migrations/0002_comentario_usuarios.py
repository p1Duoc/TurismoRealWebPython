# Generated by Django 3.0.2 on 2020-03-14 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario_Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('comentario_aprobado', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
