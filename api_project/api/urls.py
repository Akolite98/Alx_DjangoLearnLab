# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Only import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  # Use 'books' as the endpoint

urlpatterns = [
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]