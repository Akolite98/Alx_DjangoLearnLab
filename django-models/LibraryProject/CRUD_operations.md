# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Create Operation

## Output
The book "1984" by George Orwell was successfully created.

# Retrieve Operation

## Command
```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")



## Output
Title: 1984, Author: George Orwell, Year: 1949

# Update Operation

## Command
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()



## Output
The title of the book was successfully updated to "Nineteen Eighty-Four".

# Delete Operation

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


## Output
The book "Nineteen Eighty-Four" was successfully deleted.
