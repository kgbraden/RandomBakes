# Generated by Django 3.1.2 on 2020-12-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0045_auto_20201218_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
