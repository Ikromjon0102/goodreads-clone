from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='profile_pictures/default_profile_pictures.png', upload_to='profile_pictures')


