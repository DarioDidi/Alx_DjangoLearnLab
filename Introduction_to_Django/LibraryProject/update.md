gotten =  Book.objects.get(title="1984")
gotten.title = "Nineteen Eighty-Four"
gotten.save()