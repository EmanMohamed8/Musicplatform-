from django.urls import path, include
from .views import Register, Login, MainUser
from knox import views as knox_views

urlpatterns = [
    # path('authentication/', include('knox.urls')),
    path("authentication/register/", Register.as_view(), name="register_user"),
    path("authentication/login/", Login.as_view(), name="login_user"),
    path("authentication/logout/", knox_views.LogoutView.as_view(), name="knox-logout"),
]
