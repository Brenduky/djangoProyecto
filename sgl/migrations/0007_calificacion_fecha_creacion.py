# Generated by Django 4.2.1 on 2023-06-25 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sgl', '0006_rename_examen_leccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
