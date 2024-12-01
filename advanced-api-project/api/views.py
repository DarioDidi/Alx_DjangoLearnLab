from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import filters

# from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic.detail import DetailView
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer
# Create your views here.


# allows readonly unless logged in
# allows search and filter by 'author' and 'title'
class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'author', 'publication_year']

# list all books


class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    model = Book

    def get_queryset(self):
        return get_object_or_404(
            Book,
            pk=self.kwargs['pk'],
        )

# auth users can create, update, delete books


class CreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
