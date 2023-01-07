from django.contrib import admin
from .models import Album
from .models import Song
from .forms import AtLeastOneRequiredInlineFormSet


class AlbumInline(admin.TabularInline):
    model = Song
    formset = AtLeastOneRequiredInlineFormSet


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ['dateTime']
    inlines = [AlbumInline]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
