# Generated by Django 3.1.2 on 2020-10-08 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0018_auto_20201008_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='batch',
        ),
        migrations.AddField(
            model_name='orders',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='MainPage.activesales'),
            preserve_default=False,
        ),
    ]
