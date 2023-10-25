from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializers


class AlbumSerializers(serializers.ModelSerializer):
    artist = ArtistSerializers()

    class Meta:
        model = Album
        fields = ["id", "artist", "name", "release_datetime", "cost"]


class AlbumSerializersForPost(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["name", "cost", "approved"]
