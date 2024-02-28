from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
