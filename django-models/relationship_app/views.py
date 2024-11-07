from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Library, Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def list_books(request):
    results = serialize("json", Book.objects.all())
    print(results)
    return render(request, 'relationship_app/list_books.html', context={'books': results})

"from .views import list_books", "LibraryDetailView"
class LibraryDetailView(DetailView):
    # model = Library
    # template_name = "library_detail.html"
    model = Library

    def get(self, request):
        books = serialize("json", self.get_queryset().all())
        return render(request, "relationship_app/library_detail.html", context={'books': books})
