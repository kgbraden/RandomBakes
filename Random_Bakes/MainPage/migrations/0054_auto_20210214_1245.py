# Generated by Django 3.1.2 on 2021-02-14 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0053_auto_20210214_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=12),
        ),
    ]