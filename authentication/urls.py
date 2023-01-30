from django.urls import path
from .views import Register, Login, MainUser
from knox import views as knox_views

urlpatterns = [
    path('register/', Register.as_view(), name='register_user'),
    path('login/', Login.as_view(), name='login_user'),
    path('user/', MainUser.as_view(), name='user'),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]
