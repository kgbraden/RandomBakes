# Generated by Django 3.1.2 on 2020-10-29 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0027_auto_20201029_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivered',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
