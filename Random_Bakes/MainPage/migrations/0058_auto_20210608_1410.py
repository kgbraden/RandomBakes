# Generated by Django 3.1.5 on 2021-06-08 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0057_auto_20210608_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activesales',
            name='bakingdate',
            field=models.DateField(default=datetime.datetime(2021, 6, 19, 14, 10, 11, 255252)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=13),
        ),
    ]
