from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class FollowUnfollowView(generics.GenericAPIView):  # Using GenericAPIView as required
    queryset = User.objects.all()  # Using User.objects.all() as required
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user = get_object_or_404(User, pk=kwargs.get('pk'))
        
        if request.user == target_user:
            return Response(
                {"error": "You cannot follow/unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.user.following.filter(pk=target_user.pk).exists():
            request.user.following.remove(target_user)
            return Response(
                {"message": f"You have unfollowed {target_user.username}"},
                status=status.HTTP_200_OK
            )
        else:
            request.user.following.add(target_user)
            return Response(
                {"message": f"You are now following {target_user.username}"},
                status=status.HTTP_200_OK
            )