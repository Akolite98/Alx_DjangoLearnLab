from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser  # or User if that's your model name
from .serializers import UserSerializer

class FollowUnfollowView(generics.GenericAPIView):
    # Use your exact custom user model name here
    queryset = CustomUser.objects.all()  # Changed from User to CustomUser
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user = get_object_or_404(CustomUser, pk=kwargs.get('pk'))  # Changed here too
        
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