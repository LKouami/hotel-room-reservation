# Generated by Django 4.0.3 on 2022-04-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentmodule', '0007_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
