from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import *
from django.views.generic import ListView
# Create your views here.


def list_books(request):
    results = serialize("json", Book.objects.all())
    print(results)
    return render(request, 'list_books.html', context={'books': results})


class displayLibrary(ListView):
    # model = Library
    # template_name = "library_detail.html"
    model = Book

    def get(self, request):
        books = serialize("json", self.get_queryset().all())
        return render(request, "library_detail.html", context={'books': books})
