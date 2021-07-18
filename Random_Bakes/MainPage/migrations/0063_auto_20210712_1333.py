# Generated by Django 3.1.5 on 2021-07-12 20:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0062_auto_20210608_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomBakeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(blank=True)),
                ('story', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='RandomBake_images')),
                ('amount', models.CharField(max_length=80)),
                ('cost', models.DecimalField(decimal_places=2, default=5.0, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='activesales',
            name='bakingdate',
            field=models.DateField(default=datetime.datetime(2021, 7, 24, 13, 33, 29, 872110)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivorder',
            field=models.PositiveIntegerField(default=12),
        ),
        migrations.AddField(
            model_name='activesales',
            name='rbItem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='RB_Item', to='MainPage.randombakeitem'),
        ),
    ]
