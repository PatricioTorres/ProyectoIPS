# Generated by Django 3.0.8 on 2020-07-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20200723_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='fecha_inicio',
            field=models.CharField(max_length=10),
        ),
    ]
