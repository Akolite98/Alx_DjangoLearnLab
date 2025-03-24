from django.urls import path
from .views import follow_user, unfollow_user  # Make sure these views exist

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]