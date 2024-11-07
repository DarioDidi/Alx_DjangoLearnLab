from django.contrib import admin
from django.urls import path
from .views import LibraryDetailView
from .views import list_books
urlpatterns = [
    path('listbooks/', list_books, name="list_books"),
    path('displaylibrary/', LibraryDetailView.as_view(), name="display_library"),
]
