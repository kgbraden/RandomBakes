# Generated by Django 3.1.2 on 2020-10-09 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0021_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='MainPage.activesales'),
        ),
    ]
