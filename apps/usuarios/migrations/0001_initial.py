# Generated by Django 3.0.8 on 2020-07-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=50)),
                ('nombre_comercial', models.CharField(max_length=50)),
                ('ruc', models.IntegerField()),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('fecha_inicio', models.DateField()),
            ],
        ),
    ]
