from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.core.serializers import serialize

# Create your views here.


from .models import Book


@permission_required('bookshelf.can_create', raise_exception=True)
def create(request):
    pass


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
