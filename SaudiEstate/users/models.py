from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to='users/profiles/', default='users/profiles/default.png')
    about = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username