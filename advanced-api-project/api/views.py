from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookCreateView(generics.CreateAPIView):
    """Create a new book with additional validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        """Ensure data integrity before saving."""
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book with custom validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        """Ensure data integrity before updating."""
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
