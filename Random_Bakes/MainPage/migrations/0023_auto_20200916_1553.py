# Generated by Django 3.1 on 2020-09-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0022_auto_20200916_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurette',
            name='title',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
