from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/<int:pk>', views.Userpk.as_view())
]
