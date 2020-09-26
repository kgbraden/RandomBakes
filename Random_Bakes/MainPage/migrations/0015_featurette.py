# Generated by Django 3.1 on 2020-09-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0014_highlight_button_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featurette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, unique=True)),
                ('description', models.CharField(max_length=430)),
                ('Story', models.TextField(default='None')),
                ('photo', models.ImageField(default='/media/photo-placeholder-icon.jpg', upload_to='highlight_images')),
                ('button', models.CharField(max_length=18)),
                ('button_link', models.CharField(default='#', max_length=264)),
                ('button_class', models.CharField(default='btn btn-lg btn-primary cover-heading', max_length=264)),
            ],
        ),
    ]