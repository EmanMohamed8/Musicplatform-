from django.shortcuts import render
from .forms import AlbumForm
# Create your views here.


def create(requset):
    if requset.method == 'POST':
        dataForm = AlbumForm(requset.POST)
        if (dataForm.is_valid):
            dataForm.save()
    return render(requset, 'albums/create.html', {'form': AlbumForm})
