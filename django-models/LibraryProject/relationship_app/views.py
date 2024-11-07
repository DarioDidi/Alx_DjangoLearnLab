from django.contrib.auth.forms import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import *
from django.views.generic import ListView
from .forms import RegistrationForm
# Create your views here.


def list_books(request):
    results = serialize("json", Book.objects.all())
    print(results)
    return render(request, 'relationship_app/list_books.html', context={'books': results})


class displayLibrary(ListView):
    # model = Library
    # template_name = "library_detail.html"
    model = Book

    def get(self, request):
        books = serialize("json", self.get_queryset().all())
        return render(request, "relationship_app/library_detail.html", context={'books': books})


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', context={'form': form})
