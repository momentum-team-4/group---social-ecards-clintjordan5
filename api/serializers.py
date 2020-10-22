from users.models import User
from .models import Card
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = [
            'author',
            'title',
            'body',
            'date',   
        ]

class FollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'follow',
            'friends',
        ]

class FriendRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'proposing_user',
            'accepting_user',
        ]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'author',
            'card',
            'comment_text',
        ]