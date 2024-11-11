from django.contrib import admin
from django.urls import path, include
from .views import list_books, displayLibrary, sign_up

urlpatterns = [
    path('listbooks/', list_books, name="list_books"),
    path('displaylibrary/', displayLibrary.as_view(), name="display_library"),
    path('', include('django.contrib.auth.urls')),
    path('register/', sign_up, name='register'),
]
