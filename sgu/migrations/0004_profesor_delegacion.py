# Generated by Django 4.2.1 on 2023-06-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0003_alumno_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='delegacion',
            field=models.CharField(choices=[('ALVARO', 'Álvaro Obregón'), ('AZCAPOTZALCO', 'Azcapotzalco'), ('BENITO', 'Benito Juárez'), ('COYOACAN', 'Coyoacán'), ('CUAJIMALPA', 'Cuajimalpa de Morelos'), ('CUAUHTEMOC', 'Cuauhtémoc'), ('GUSTAVO', 'Gustavo A. Madero'), ('IZTACALCO', 'Iztacalco'), ('IZTAPALAPA', 'Iztapalapa'), ('MAGDALENA', 'La Magdalena Contreras'), ('MIGUEL', 'Miguel Hidalgo'), ('MILPA', 'Milpa Alta'), ('TLAHUAC', 'Tláhuac'), ('TLALPAN', 'Tlalpan'), ('VENUSTIANO', 'Venustiano Carranza'), ('XOCHIMILCO', 'Xochimilco')], default='ALVARO', max_length=100),
            preserve_default=False,
        ),
    ]