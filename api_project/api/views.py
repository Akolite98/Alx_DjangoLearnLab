from rest_framework.generics import ListAPIView  # Ensure this import exists
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Ensure the class extends ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
