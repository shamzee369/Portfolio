from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return self.user.username
