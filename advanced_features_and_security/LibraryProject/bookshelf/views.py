from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.core.serializers import serialize

# Create your views here.

from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_create', raise_exception=True)
def create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid:
            content = form.cleaned_data
            b = Book.objects.create(
                name=form.name, publication_year=form.publication_year)
            b.save()
            return redirect("")
    else:
        form = ExampleForm
    return render(request, 'form_example.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit(request):
    pass


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete(request):
    pass


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    results = serialize("json", Book.objects.all())
    print(results)
    return render(request, 'bookshelf/book_list.html', context={'books': results})
