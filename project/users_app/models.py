from django.db import models
from .models import Users

class Users(models.Model):
    username = models.CharField(max_length=8)
    phoneNumber = models.IntegerField(default=0)
    createdAt = models.DateTimeField("when user is created")
    