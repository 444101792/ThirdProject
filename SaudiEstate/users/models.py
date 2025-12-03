from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
        CITIES = [
       ('Riyadh', 'Riyadh'),
       ('Jeddah', 'Jeddah'),
       ('Dammam', 'Dammam'),
       ('Khobar', 'Khobar'),
       ('Makkah', 'Makkah'),
       ('Madina', 'Madina'),
       ('Abha', 'Abha'),
       ('Tabuk', 'Tabuk'),
       ('Qassim', 'Qassim'),
       ('Hail', 'Hail'),
       ('Najran', 'Najran'),
       ('Jazan', 'Jazan'),
       ('Buraidah', 'Buraidah'),
       ('Al-Ahsa', 'Al-Ahsa'),
       ('Taif', 'Taif'),
       ('Baha', 'Baha')
    ]
        
        phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
        country_code = models.CharField(max_length=10, default="+966")
        city = models.CharField(max_length=100, choices=CITIES, null=True, blank=True)
        profile_image = models.ImageField(upload_to='users/profiles/', default='users/profiles/default.png')
        about = models.TextField(blank=True, null=True)

        def __str__(self):
            return self.username