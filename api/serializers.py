from users.models import User
from .models import Card
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = [
            'author',
            'date',   
        ]
        # url? id? author? message?

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'follow'
            'friends'
        ]