# Generated by Django 3.2 on 2022-06-08 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0002_tipo_ruta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='tipo_ruta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.tipo_ruta'),
        ),
    ]
