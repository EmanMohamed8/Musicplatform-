from django.shortcuts import render
# from .forms import AlbumForm
from django.views.generic import CreateView, ListView
from .models import Album
from django.urls import reverse


class AlbumList(ListView):
    model = Album


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'name', 'dateTime', 'cost']

    def get_success_url(self):
        return reverse('create_album')