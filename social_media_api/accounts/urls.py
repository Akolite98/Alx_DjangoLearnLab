from django.urls import path
from .views import FollowUnfollowView

urlpatterns = [
    path('users/<int:pk>/follow/', FollowUnfollowView.as_view(), name='follow-unfollow'),
]