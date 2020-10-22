from users.models import User
from .models import Card
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'author',
            'title',
            'body',
            'date',   
        ]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'follow',
            'friends',
        ]

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'proposing_user',
            'accepting_user',
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'author',
            'card',
            'comment_text',
        ]

# hyperlinked model serializer broke the internet. switched to modelserializer and fixed URL errors. 