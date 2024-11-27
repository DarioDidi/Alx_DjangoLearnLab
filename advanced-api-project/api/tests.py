from django.test import TestCase
from .models import Book, Author
# Create your tests here.


class AuthorTest(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name='a1')
        author.save()

    # def test_book_creation(self):
        author = Author.objects.get(name='a1')
        book = Book.objects.create(
            title='b1', publication_year=2016, author=author)
        book.save()

# class BooksTest(TestCase):
