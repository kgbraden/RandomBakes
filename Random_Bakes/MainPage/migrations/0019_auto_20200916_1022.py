# Generated by Django 3.1 on 2020-09-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0018_auto_20200914_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurette',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='featurette',
            name='type',
            field=models.CharField(default='index', max_length=35),
        ),
    ]
