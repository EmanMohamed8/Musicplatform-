from django.shortcuts import render
from albums.models import Album
from .models import Artist
from django.urls import reverse
from django.db.models import Count
from django.views.generic import CreateView, ListView

class ArtistList(ListView):
    model = Artist
    queryset = Artist.objects.all().values('id', 'stageName', 'socialLink', 'art_album__approved').annotate(
        approved_albums=Count('art_album', filter=('art_album__approved' == True))).order_by('approved_albums')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album_detils'] = Album.objects.filter(
            approved=True).values('id', 'name', 'dateTime', 'cost', 'artist')
        return context


class ArtistCreate(CreateView):
    model = Artist
    fields = ['stageName', 'socialLink']
    def get_success_url(self):
        return reverse('create_artist')
