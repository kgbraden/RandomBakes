# Generated by Django 3.1.2 on 2020-10-08 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0004_auto_20201007_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Fname',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Lname',
            new_name='Last_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dCity',
            new_name='delivery_City',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dState',
            new_name='delivery_State',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dStreet1',
            new_name='delivery_Street1',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dStreet2',
            new_name='delivery_Street2',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dZip',
            new_name='delivery_Zip',
        ),
    ]