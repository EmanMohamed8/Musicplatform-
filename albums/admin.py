from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['dateTime']


admin.site.register(Album, AlbumAdmin)
