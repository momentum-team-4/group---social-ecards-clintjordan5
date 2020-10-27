from django.contrib import admin
from .models import Card, FollowedUsers, Comment

admin.site.register(Card)
admin.site.register(FollowedUsers)
admin.site.register(Comment)
