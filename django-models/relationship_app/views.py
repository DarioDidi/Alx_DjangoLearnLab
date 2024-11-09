from django.shortcuts import render, redirect
# from django.http import JsonResponse
from django.core.serializers import serialize

# from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import views
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import permission_required, user_passes_test
# Create your views here.

from .models import Library, Book, UserProfile


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
    return render(request, "relationship_app/register.html", {"form": UserCreationForm})


def role_check(user):
    profile = UserProfile.objects.get(user=user)
    return profile.role
# @permission_required('relationship_app.Admin')


@user_passes_test(role_check == "Admin")
def admin_view(request):
    pass


@user_passes_test(role_check == "Librarian")
def librarian_view(request):
    pass


@user_passes_test(role_check == "Member")
def member_view(request):
    pass
