# Generated by Django 2.2.7 on 2020-01-01 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0003_viaje_site_destino_origen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='razon_excepcion',
            field=models.TextField(default='Sin espesificar'),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='tipo_viaje',
            field=models.CharField(default='sin espesificar', max_length=30),
        ),
        migrations.AlterField(
            model_name='viajeadministrativo',
            name='vendor',
            field=models.ForeignKey(default='Sin espesificar', null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.Vendor'),
        ),
    ]