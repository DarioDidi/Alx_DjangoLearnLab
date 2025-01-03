from django.shortcuts import render, redirect
# from django.http import JsonResponse
from django.core.serializers import serialize

# from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import views
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
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


def admin_check(user):
    profile = UserProfile.objects.get(user=user)
    return profile.role == "Admin"


def librarian_check(user):
    profile = UserProfile.objects.get(user=user)
    return profile.role == "Librarian"


def member_check(user):
    profile = UserProfile.objects.get(user=user)
    return profile.role == "Member"


@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(member_check)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# creation, modification, and deletion.
@permission_required('relationship_app.can_add_book')
def add_book(request):
    pass


@permission_required('relationship_app.can_change_book')
def edit_book(request):
    pass


@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    pass
