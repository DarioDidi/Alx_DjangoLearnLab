from bookshelf.models import Book
b = Book.objects.get(title="1984")
vars(b)
{'_state': <django.db.models.base.ModelState object at 0x71c894671cf0>, 'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}