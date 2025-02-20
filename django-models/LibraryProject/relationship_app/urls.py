from django.urls import path
from .views import list_books, LibraryDetailView  # Import both views

urlpatterns = [
    # URL pattern for the function-based view (list_books)
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view (LibraryDetailView)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]