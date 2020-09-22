# Generated by Django 3.1 on 2020-09-21 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='baking_batch',
            fields=[
                ('batch_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('batch_date', models.DateField()),
                ('batch_type', models.CharField(max_length=100)),
                ('room_temp', models.DecimalField(decimal_places=1, max_digits=4)),
                ('room_humid', models.DecimalField(decimal_places=1, max_digits=4)),
                ('batch_photo', models.ImageField(default='/media/photo-placeholder-icon.jpg', upload_to='batch_images')),
                ('batch_final_notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreFerment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ferm_started', models.TimeField()),
                ('ferm_temp_start', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ferm_temp_fermented', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ferm_temp_after_retardation', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ferm_final_weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ferm_notes', models.TextField(default='None')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipes.baking_batch')),
                ('ferm_ingredients', models.ManyToManyField(to='Recipes.fermIngredients')),
            ],
        ),
    ]
