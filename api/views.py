from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from .serializers import CardSerializer, FollowSerializer, FriendRequestSerializer, CommentSerializer, UserSerializer
from .models import Card, Comment, FriendRequest, Follow
from users.models import User
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.exceptions import ParseError

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
        if obj.author == request.user:
            return True

        return False

class IsPostAuthor(BasePermission):
    def has_permission(self, request, view):
        return True
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.author

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Card.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def all_cards(self, request):
        cards = Card.objects.all()
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)

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
        return Follow.objects.all()

    def perform_create(self, serializer):
        return serializer.save(id=self.request.user)

class FriendRequestViewSet(ModelViewSet):
    serializer_class = FriendRequestSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return FriendRequest.objects.all()

    def perform_create(self, serializer):
        return serializer.save(proposing_user=self.request.user)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return User.objects.all()

class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostAuthor]
    parser_classes = [JSONParser, FileUploadParser]

    @action(detail=True, methods=['PUT'])
    def image(self, request, pk, format=None):
        if 'file' not in request.data:
            raise ParseError('Empty content')

        file = request.data['file']
        post = self.get_object()

        post.image.save(file.name, file, save=True)
        return Response(status=201)