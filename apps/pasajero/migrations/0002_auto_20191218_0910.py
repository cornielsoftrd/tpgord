# Generated by Django 2.2.7 on 2019-12-18 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasajero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='direccion',
            field=models.CharField(max_length=150),
        ),
    ]
