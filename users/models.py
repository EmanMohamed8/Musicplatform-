from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=256, blank=True)
    text_area = models.TextField(max_length=3000, blank=True)
