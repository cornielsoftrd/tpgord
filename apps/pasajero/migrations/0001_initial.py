# Generated by Django 2.2.7 on 2019-12-07 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ruta', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cuenta', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id_pasajero', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50, null=True, unique=True)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('Ruta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='ruta.Ruta')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pasajero.Cuenta')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
    ]
