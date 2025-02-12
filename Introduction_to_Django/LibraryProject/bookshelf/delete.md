# Delete Operation

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


## Output
The book "Nineteen Eighty-Four" was successfully deleted.