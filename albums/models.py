from datetime import datetime
from email.policy import default
from hashlib import blake2b
from pyexpat import model
from statistics import mode
from tokenize import blank_re
from unicodedata import name
from django.db import models
from artists.models import Artist


class Album (models.Model):
    artist = models.ForeignKey(
        Artist, null=False, on_delete=models.CASCADE, related_name='art_album')
    name = models.CharField(max_length=50, default='New Album')
    dateTime = models.DateTimeField(default=datetime.now)
    cost = models.FloatField(blank=False)

    def __str__(self) -> str:
        return self.name
