from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomUser

@api_view(['POST'])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    
    if request.user == target_user:
        return Response(
            {"error": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.add(target_user)
    return Response(
        {"message": f"You are now following {target_user.username}"},
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    
    if request.user == target_user:
        return Response(
            {"error": "You cannot unfollow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    request.user.following.remove(target_user)
    return Response(
        {"message": f"You have unfollowed {target_user.username}"},
        status=status.HTTP_200_OK
    )