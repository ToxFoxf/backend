from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=8)
    age = models.IntegerField(default=0)
    createdAt = models.DateTimeField("when user is created")
    