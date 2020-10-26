from django.db import models
from django.db.models.fields.related import ManyToManyField
from users.models import User
from rest_framework.authtoken.models import Token


COLOR_OPTIONS = (
    ("black", "black"),
    ("blue", "blue"),
    ("red", "red"),
    ("none", "none"),
)

BORDER_OPTIONS = (
    ("solid", "solid"),
    ("dotted", "dotted"),
    ("none", "none"),
)

FONT_OPTIONS = (
    ("Times New Roman", "Times New Roman"),
    ("Helvetica", "Helvetica"),
    ("Open Sans", "Open Sans"),
    ("none", "none"),
)


class Card(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="cards", null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    color = models.CharField(max_length=100, choices=COLOR_OPTIONS, default="", null=True)
    border = models.CharField(max_length=100, choices=BORDER_OPTIONS, default="", null=True)
    font = models.CharField(max_length=100, choices=FONT_OPTIONS, default="", null=True)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)


class Follow(models.Model):
    followed_users = models.ManyToManyField("self", related_name="followers", null=True)
    # friends = models.ManyToManyField("self", symmetrical=True)


class FriendRequest(models.Model):
    proposing_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="friendrequests", null=True)
    accepting_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="acceptedrequests", null=True)


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments", null=True)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE, related_name="comments", null=True)
    comment_text = models.TextField(null=True, blank=True)
