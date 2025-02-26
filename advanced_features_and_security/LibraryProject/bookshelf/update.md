# Update Operation

## Command
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()



## Output
The title of the book was successfully updated to "Nineteen Eighty-Four".