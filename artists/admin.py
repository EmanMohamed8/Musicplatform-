from django.contrib import admin
from .models import Artist

class artistAlbum:
    list_display = ['stageName']


admin.site.register(Artist)