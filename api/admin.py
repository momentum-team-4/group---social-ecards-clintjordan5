from django.contrib import admin
from .models import Card, User, FriendRequest, Comment

admin.site.register(Card)
admin.site.register(User)
admin.site.register(FriendRequest)
admin.site.register(Comment)
