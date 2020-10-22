from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from .serializers import CardSerializer, UserSerializer
from .models import Card

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
