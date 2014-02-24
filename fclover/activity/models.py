from django.db import models

from account.models import UserProfile

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=1000)
    picture = models.CharField(max_length=100)
    content = models.TextField(max_length=10000, default="", blank=True)
    initiator = models.OneToOneField(UserProfile)
    participant = models.ManyToManyField(UserProfile, related_name='activity_users')
    createTime = models.DateTimeField()
    dueTime = models.DateTimeField()
    beginTime = models.DateTimeField()
    endTime = models.DateTimeField()
    location = models.CharField(max_length=100)
    maxMale = models.IntegerField()
    maxFemale = models.IntegerField()
    type = models.IntegerField()
