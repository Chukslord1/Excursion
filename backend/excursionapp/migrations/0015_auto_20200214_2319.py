# Generated by Django 3.0 on 2020-02-15 07:19

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('excursionapp', '0014_auto_20200214_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='typology',
            field=django_mysql.models.ListCharField(models.CharField(max_length=9), max_length=20, size=2),
        ),
    ]