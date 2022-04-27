# Generated by Django 4.0.3 on 2022-04-26 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentmodule', '0004_car_price_reservation_bill'),
        ('authentication', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reservations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentmodule.reservation'),
        ),
    ]
