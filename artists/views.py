from django.shortcuts import render
from albums.models import Album
from .models import Artist
from django.db.models import Count

def artist(requset):
        objects = Artist.objects.all().values('id', 'stageName', 'socialLink', 'art_album__approved').annotate(
            total_approved=Count('art_album', filter='art_album__approved' == True)).order_by('-total_approved')
        objects2 = Album.objects.filter(approved=True).values(
            'id', 'name', 'dateTime', 'cost', 'artist')
        return render(requset, 'artists/artist.html', {'art': objects, 'art2': objects2})
