from datetime import datetime
from email.policy import default
from hashlib import blake2b
from pyexpat import model
from statistics import mode
from tokenize import blank_re
from unicodedata import name
from django.db import models
from artists.models import Artist
from django.urls import reverse
from imagekit.models import ImageSpecField
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Album (models.Model):
    artist = models.ForeignKey(
        Artist, null=False, on_delete=models.CASCADE, related_name='art_album')
    name = models.CharField(max_length=50, default='New Album')
    dateTime = models.DateTimeField(default=datetime.now)
    cost = models.FloatField(blank=False)
    approved = models.BooleanField(
        default=False, help_text=' Approve the album if its name is not explicit')

    def __str__(self) -> str:
        return self.name


class Song (models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=False, related_name='song_album')
    song_name = models.CharField(max_length=50, default='song_album__name')
    song_image = models.ImageField(upload_to='images/%y/%m/%d', null=True)
    thumbnail_image = ImageSpecField(source='song_image', format='JPEG')
    song_audio = models.FileField(upload_to='music/', null=True)
