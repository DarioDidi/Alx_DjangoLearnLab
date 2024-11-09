from django.contrib import admin
from django.urls import path, include
from .views import LibraryDetailView
from .views import list_books
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('listbooks/', list_books, name="list_books"),
    path('displaylibrary/', LibraryDetailView.as_view(), name="display_library"),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name="registration/login"), name="login"),
    path('logout', LogoutView.as_view(template_name="registration/logout"), name="logout"),
]
