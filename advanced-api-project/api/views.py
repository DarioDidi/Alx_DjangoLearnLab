from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from django.views.generic.detail import DetailView

from .models import Book
from .serializers import BookSerializer
# Create your views here.


class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(generics.RetrieveAPIView):
    model = Book

    def get_queryset(self):
        return get_object_or_404(
            Book,
            pk=self.kwargs['pk'],
        )


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
