from django.urls import path, include
from .views import register, profile, DisplayPosts, UserPosts
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", DisplayPosts.as_view(), name="home"),
    path("posts", UserPosts.as_view(), name='posts'),
    path("register/", register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("profile/", profile, name="profile")
]
