# Generated by Django 3.1.2 on 2020-10-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0014_auto_20201008_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
