from django.contrib import admin
from .models import Book

# Register your models here.
admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')
    search_fields = ('author', 'title', "year")
    list_filter = ('title')