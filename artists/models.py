from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Artist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='artist')
    stageName = models.CharField(max_length=50, unique=True, blank=False)
    socialLink = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.stageName

    class Meta:
        ordering = ['stageName']
