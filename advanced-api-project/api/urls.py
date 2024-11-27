from django.urls import path
from views import *
urlpatterns = [
    path('/books/', ListView.as_view(), name='list'),
    path('/books/<int:pk>/', DetailView.as_view(), name='detail'),
    path('/books/create', CreateView.as_view, name='create'),
    path('/books/update', UpdateView.as_view, name='update'),
    path('/books/delete', DeleteView.as_view, name='delete'),
]
