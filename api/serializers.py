from re import T
from users.models import User
from .models import Card, Comment, FollowedUsers
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

# class FollowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Follow
#         fields = [
#             'url',
#             'followed_users',
#         ]

class FollowedUserSerializer(serializers.ModelSerializer):
    proposing_user = serializers.StringRelatedField(read_only=True)
    following= serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = FollowedUsers
        fields = [
            'proposing_user',
            'following',
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