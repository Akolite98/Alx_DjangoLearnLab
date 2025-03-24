from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet

router = DefaultRouter()
router.register(r'users', FollowViewSet, basename='user-follow')

urlpatterns = [
    path('', include(router.urls)),
]