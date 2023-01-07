from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('albums/', views.AlbumList.as_view(), name='album'),
    path('create/', login_required(views.AlbumCreate.as_view()), name='create_album'),
]
