from .models import *

author = Author.get(name="a")
books = Book.objects.get(author=author)
library = Library.get(name="a")
books = Book.objects.get(library=library)
librarian = Librarian.objects.get(library=library)