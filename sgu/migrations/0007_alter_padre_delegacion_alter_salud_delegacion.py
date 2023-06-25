# Generated by Django 4.2.1 on 2023-06-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgu', '0006_remove_padre_numero_de_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='padre',
            name='delegacion',
            field=models.CharField(choices=[('ALVARO', 'Álvaro Obregón'), ('AZCAPOTZALCO', 'Azcapotzalco'), ('BENITO', 'Benito Juárez'), ('COYOACAN', 'Coyoacán'), ('CUAJIMALPA', 'Cuajimalpa de Morelos'), ('CUAUHTEMOC', 'Cuauhtémoc'), ('GUSTAVO', 'Gustavo A. Madero'), ('IZTACALCO', 'Iztacalco'), ('IZTAPALAPA', 'Iztapalapa'), ('MAGDALENA', 'La Magdalena Contreras'), ('MIGUEL', 'Miguel Hidalgo'), ('MILPA', 'Milpa Alta'), ('TLAHUAC', 'Tláhuac'), ('TLALPAN', 'Tlalpan'), ('VENUSTIANO', 'Venustiano Carranza'), ('XOCHIMILCO', 'Xochimilco')], max_length=100),
        ),
        migrations.AlterField(
            model_name='salud',
            name='delegacion',
            field=models.CharField(choices=[('ALVARO', 'Álvaro Obregón'), ('AZCAPOTZALCO', 'Azcapotzalco'), ('BENITO', 'Benito Juárez'), ('COYOACAN', 'Coyoacán'), ('CUAJIMALPA', 'Cuajimalpa de Morelos'), ('CUAUHTEMOC', 'Cuauhtémoc'), ('GUSTAVO', 'Gustavo A. Madero'), ('IZTACALCO', 'Iztacalco'), ('IZTAPALAPA', 'Iztapalapa'), ('MAGDALENA', 'La Magdalena Contreras'), ('MIGUEL', 'Miguel Hidalgo'), ('MILPA', 'Milpa Alta'), ('TLAHUAC', 'Tláhuac'), ('TLALPAN', 'Tlalpan'), ('VENUSTIANO', 'Venustiano Carranza'), ('XOCHIMILCO', 'Xochimilco')], max_length=100),
        ),
    ]
