<!-- create -->
from bookshelf.models import Book
b = Book(title="1984", author="George Orwell", publication_year=1949)
b.save()
<!-- retrieve -->
b = Book.objects.get(title="1984")
vars(b)
<!-- {'_state': <django.db.models.base.ModelState object at 0x71c894671cf0>, 'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949} -->

<!-- update -->
gotten =  Book.objects.get(title="1984")
gotten.title = "Nineteen Eighty-Four"
gotten.save()
<!-- delete -->
Book.objects.filter(title="Nineteen Eighty-Four").delete()
<!-- (1, {'bookshelf.Book': 1}) -->