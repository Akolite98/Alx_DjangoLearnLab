# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

## Output
The book "Nineteen Eighty-Four" was successfully deleted.