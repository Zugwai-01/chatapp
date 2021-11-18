from django.db import models
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=10000000)
    user = models.CharField(max_length=10000000)