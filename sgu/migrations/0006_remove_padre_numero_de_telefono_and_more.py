# Generated by Django 4.2.1 on 2023-06-24 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0005_salud_padre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='padre',
            name='numero_de_telefono',
        ),
        migrations.RemoveField(
            model_name='salud',
            name='numero_de_telefono',
        ),
    ]
