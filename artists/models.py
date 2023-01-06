from email.policy import default
from statistics import mode
from django.db import models


class Artist(models.Model):
    stageName = models.CharField(max_length=50, unique=True, blank=False)
    socialLink = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.stageName

    class Meta:
        ordering = ['stageName']
