# Generated by Django 2.2.7 on 2019-12-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportista', '0002_auto_20191207_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportista',
            name='codigo_transportista',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
