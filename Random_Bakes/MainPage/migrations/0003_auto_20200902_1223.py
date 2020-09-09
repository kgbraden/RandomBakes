# Generated by Django 3.1 on 2020-09-02 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainPage', '0002_auto_20200902_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='photo2',
            field=models.ImageField(default='/media/photo-placeholder-icon.jpg', upload_to='highlight_images'),
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]