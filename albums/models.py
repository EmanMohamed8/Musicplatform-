from datetime import datetime
from django.db import models
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        null=False,
        blank=True,
        on_delete=models.CASCADE,
        related_name="art_album",
    )
    name = models.CharField(max_length=50, default="New Album")
    release_datetime = models.DateTimeField(default=datetime.now, blank=True)
    cost = models.FloatField(blank=False)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
