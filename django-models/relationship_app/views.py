from django.shortcuts import render, redirect
# from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Library, Book
# from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import views
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# views.register(LogoutView.as_view(template_name=", "LoginView.as_view(template_name="

def list_books(request):
    results = serialize("json", Book.objects.all())
    print(results)
    return render(request, 'relationship_app/list_books.html', context={'books': results})




class LibraryDetailView(DetailView):
    # model = Library
    # template_name = "library_detail.html"
    model = Library

    def get(self, request):
        books = serialize("json", self.get_queryset().all())
        return render(request, "relationship_app/library_detail.html", context={'books': books})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(response, "register/register.html", {"form": UserCreationForm})
