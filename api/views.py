from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"ok": True})

# will need to make a user view, followed view, and display all cards

# class CardViewSet

# class FollowedViewSet

# class ListViewSet