from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('albums/', views.AlbumsList.as_view()),
]
