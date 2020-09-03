from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class highlight(models.Model):
    title = models.CharField(max_length = 35, unique = True)
    story = models.CharField(max_length = 300)
    photo = models.CharField(max_length = 264)
    photo2 = models.ImageField(upload_to='highlight_images', default = '/media/photo-placeholder-icon.jpg')
    photo_alt = models.CharField(max_length = 25)
    button = models.CharField(max_length = 18)
    button_link = models.CharField(max_length = 264)
    def __str__(self):
        return self.title

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
