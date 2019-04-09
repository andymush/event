from django.db import models
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=40)
    venue = models.CharField(max_length=35)
    time = models.TimeField()
    fee = models.CharField(max_length=4)
    date = models.DateField()
    contact = models.CharField(max_length=10)
    cover = models.FileField()


class Comment(models.Model):
    email = models.EmailField()
    comment = models.TextField()
    time = models.DateTimeField(timezone.now)
