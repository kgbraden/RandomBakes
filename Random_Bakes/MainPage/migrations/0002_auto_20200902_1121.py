# Generated by Django 3.1 on 2020-09-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='button',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='button_link',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='photo',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='photo_alt',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='story',
            field=models.CharField(max_length=300),
        ),
    ]
