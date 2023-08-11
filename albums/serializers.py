from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializers


class AlbumSerializers(serializers.ModelSerializer):
    artist = ArtistSerializers()

    class Meta:
        model = Album
        fields = ["id", "artist", "name", "release_datetime", "cost"]
