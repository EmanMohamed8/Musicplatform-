from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>', login_required(views.ArtistPk.as_view()))
]
