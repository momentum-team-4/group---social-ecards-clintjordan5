from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from .serializers import CardSerializer, FollowSerializer, FriendRequestSerializer, CommentSerializer
from .models import Card, Comment, FriendRequest, Follow

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"ok": True})

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user:
            return True

        return False

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Card.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied()
        serializer.save(user=self.request.user)

class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Follow.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class FriendRequestViewSet(ModelViewSet):
    serializer_class = FriendRequestSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return FriendRequest.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return User.objects.all()