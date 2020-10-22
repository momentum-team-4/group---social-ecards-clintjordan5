from django.contrib import admin
from .models import Card, Follow, FriendRequest, Comment

admin.site.register(Card)
admin.site.register(FriendRequest)
admin.site.register(Comment)
admin.site.register(Follow)
