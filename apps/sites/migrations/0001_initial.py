# Generated by Django 2.2.7 on 2020-02-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id_site', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_site', models.CharField(max_length=50)),
            ],
        ),
    ]
