from django.db import models
from users.models import User
# from rest_framework.authtoken.models import Token

# Create your models here.

class Card(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cards', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

"""
model ideas
e-card will need:
author
date time field
message/title/body
"""