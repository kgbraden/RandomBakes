# Generated by Django 3.1.2 on 2021-01-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0051_auto_20210101_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurette',
            name='description',
            field=models.TextField(blank=True, default='Description goes here.'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
