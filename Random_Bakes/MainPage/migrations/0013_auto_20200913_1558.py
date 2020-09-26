# Generated by Django 3.1 on 2020-09-13 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0012_auto_20200913_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='activesales',
            name='bakingdate',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='activesales',
            name='bakingtime',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='activesales',
            name='deliverydate',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]