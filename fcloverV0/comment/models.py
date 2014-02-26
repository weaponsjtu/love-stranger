from django.db import models

from fclover.account.models import UserProfile
from fclover.activity.models import Activity

# Create your models here.

class CommentU2A(models.Model):
    user = models.OneToOneField(UserProfile)
    activity = models.ForeignKey(Activity, related_name='comment_set')
    content = models.TextField(max_length=10000)
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
    score = models.FloatField()


class CommentU2U(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sender_set')
    receiver = models.OneToOneField(UserProfile)
    score = models.FloatField()
    time = models.DateTimeField(auto_now=True, auto_now_add=True)

class MessageU2U(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='user_set')
    receiver = models.OneToOneField(UserProfile)
    content = models.TextField(max_length=10000)
    score = models.FloatField()
    time = models.DateTimeField(auto_now=True, auto_now_add=True)

class MessageU2A(models.Model):
    user = models.OneToOneField(UserProfile)
    activity = models.ForeignKey(Activity, related_name='message_set')
    content = models.TextField(max_length=10000)
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
