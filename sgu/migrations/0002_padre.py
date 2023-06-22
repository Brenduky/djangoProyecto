# Generated by Django 4.2.1 on 2023-06-22 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('delegacion', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=100)),
                ('numero_de_telefono', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
