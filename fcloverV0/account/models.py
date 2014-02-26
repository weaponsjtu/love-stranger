from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    head = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    grade = models.IntegerField()
    school = models.CharField(max_length=100)
    birthday = models.DateField()
    hobby = models.CharField(max_length=1000)
