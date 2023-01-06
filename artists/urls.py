from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist, name='artist'),
    path('artists/create/', views.create, name='create'),
]
