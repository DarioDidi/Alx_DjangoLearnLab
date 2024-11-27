from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from django.views.generic.detail import DetailView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import filters

from .models import Book
from .serializers import BookSerializer
# Create your views here.


# allows readonly unless logged in
# allows search and filter by 'author' and 'title'
class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'author', 'publication_year']


class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Book

    def get_queryset(self):
        return get_object_or_404(
            Book,
            pk=self.kwargs['pk'],
        )


class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
