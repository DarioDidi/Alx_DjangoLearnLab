from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.


@permission_required('bookshelf.can_create', raise_exception=True)
def create(request):
    pass


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit(request):
    pass


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete(request):
    pass
