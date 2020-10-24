from users.models import User
from .models import Card, Comment, Follow, FriendRequest
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
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
        model = Follow
        fields = [
            'follow',
            'friends',
        ]

class FriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = [
            'proposing_user',
            'accepting_user',
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'author',
            'card',
            'comment_text',
        ]

class UserSerializer(serializers.ModelSerializer):
    cards = serializers.RelatedField(many=True, read_only=True)
    comments = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "id", "url", "cards", "comments"]

# hyperlinked model serializer broke the internet. switched to modelserializer and fixed URL errors. 