from django.contrib import admin
from .models import Artist
from albums.models import Album

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0


class ArtistAdmin(admin.ModelAdmin):
    inlines = [
        AlbumInline
    ]


class artistAlbum:
    list_display = ['stageName']


admin.site.register(Artist, ArtistAdmin)
