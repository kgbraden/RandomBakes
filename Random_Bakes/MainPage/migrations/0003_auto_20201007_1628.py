# Generated by Django 3.1.2 on 2020-10-07 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_auto_20201007_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainPage.customer'),
        ),
    ]