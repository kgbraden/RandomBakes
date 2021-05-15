# Generated by Django 3.1.2 on 2021-02-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0052_auto_20210104_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activesales',
            name='bakingdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='activesales',
            name='bakingtime',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=6),
        ),
    ]