author_name = "a"
from .models import *
# "Author.objects.get(name=author_name)", "objects.filter(author=author)"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
books.all()
library_name = "a"
library = Library.objects.get(name=library_name)
books = Book.objects.get(library=library)
librarian = Librarian.objects.get(library=library)
