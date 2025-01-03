from django.db import models

class Robots(models.Model):
    name = models.CharField(max_length=8)
    color = models.CharField(max_length=20)
