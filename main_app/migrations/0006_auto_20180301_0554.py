# Generated by Django 2.0.2 on 2018-03-01 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20180228_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopowner',
            name='address_gps_lat',
        ),
        migrations.RemoveField(
            model_name='shopowner',
            name='address_gps_lng',
        ),
    ]