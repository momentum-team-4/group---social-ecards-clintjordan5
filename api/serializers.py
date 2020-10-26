from users.models import User
from .models import Card, Comment, Follow, FriendRequest
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Card
        fields = [
            'url',
            'author',
            'title',
            'body',
            'date',
            'color',
            'border',
            'font',
            'image',   
        ]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = [
            'url',
            'followed_users',
        ]

class FriendRequestSerializer(serializers.ModelSerializer):
    proposing_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = FriendRequest
        fields = [
            'proposing_user',
            'accepting_user',
        ]

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'url',
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

# hyperlinked model serializer caused issues. switched to modelserializer and fixed URL errors. 