# Generated by Django 4.2.1 on 2023-06-21 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0005_rename_phonenumber_padre_numero_telefono_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='padre',
            old_name='numero_telefono',
            new_name='numero_de_telefono',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='numero_telefono',
            new_name='numero_de_telefono',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='academic_degree',
            new_name='titulo_academico',
        ),
        migrations.RenameField(
            model_name='salud',
            old_name='numero_telefono',
            new_name='numero_de_telefono',
        ),
    ]
