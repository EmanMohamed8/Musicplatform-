from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist'),
    path('artists/create/', login_required(views.ArtistCreate.as_view()),name='create_artist'),
]
