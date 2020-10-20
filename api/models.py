from django.db import models
from django.db.models.fields.related import ManyToManyField
from users.models import User
# from rest_framework.authtoken.models import Token

# Create your models here.

class Card(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # color, border style, options, customizitation etc

# models below are incomplete, still building/revising 
class Message(models.Model):
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE, related_name='cards', null=True) 
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='users', null=True)
    recipient = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='users', null=True)

class User(models.Model):
    follow = models.ManyToManyField('self', related_name='followers', null=True)
    friends = models.ManyToManyField('self', symmetrical=True)

class FriendRequest(models.Model):
    proposing_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='users', null=True)
    accepting_user = models.ForeignKey (to=User, on_delete=models.CASCADE, related_name='users', null=True)
    # accepted (Boolean)


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments', null=True)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE, related_name='cards', null=True) 
