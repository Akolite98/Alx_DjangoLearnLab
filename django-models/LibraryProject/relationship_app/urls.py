from django.urls import path
from .views import list_books, LibraryDetailView  # Import both views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

        # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # URL pattern for the function-based view (list_books)
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view (LibraryDetailView)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]