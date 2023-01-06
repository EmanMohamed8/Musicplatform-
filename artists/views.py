from django.shortcuts import render
from albums.models import Album
from .models import Artist
from .forms import ArtistForm
from django.db.models import Count
# Create your views here.


def artist(requset):
    objects = Artist.objects.all().values('id', 'stageName', 'socialLink', 'art_ablum__approved').annotate(
        total_approved=Count('art_ablum', filter='art_ablum__approved' == True)).order_by('-total_approved')
    objects2 = Album.objects.filter(approved=True).values(
        'id', 'name', 'dateTime', 'artist', 'cost')
    return render(requset, 'artists/artist.html', {'art': objects, 'art2': objects2})


def create(requset):
    if requset.method == 'POST':
        dataForm = ArtistForm(requset.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(requset, 'artists/create.html', {'AF': ArtistForm})
