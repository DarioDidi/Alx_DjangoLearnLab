from .models import *
author_name = "a"
author = Author.get(name=author_name)
books = Book.objects.get(author=author)
books.all()
library_name = "a"
library = Library.objects.get(name=library_name)
books = Book.objects.get(library=library)
librarian = Librarian.objects.get(library=library)
