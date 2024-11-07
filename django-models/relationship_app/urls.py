from django.contrib import admin
from django.urls import path
from .views  import list_books, displayLibrary
urlpatterns = [
    path('listbooks/', list_books, name="list_books"),
    path('displaylibrary/', displayLibrary.as_view(), name="display_library"),
]
