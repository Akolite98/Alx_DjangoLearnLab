from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from .forms import BookSearchForm 
from django.views.decorators.csrf import csrf_protect

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})


@csrf_protect
def my_view(request):
    if request.method == "POST":
        # Handle the form submission securely
        pass
 # Assume you created a form class

def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data["title"]
        books = Book.objects.filter(title=title)
    else:
        books = Book.objects.none()  # Return an empty queryset if input is invalid
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

