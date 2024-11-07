from django.contrib import admin
from django.urls import path
from .views  import list_books 
from .views import LibraryDetailView
urlpatterns = [
    path('listbooks/', list_books, name="list_books"),
    path('displaylibrary/', LibraryDetailView.as_view(), name="display_library"),
]
