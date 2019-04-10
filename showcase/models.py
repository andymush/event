from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=40)
    venue = models.CharField(max_length=35)
    time = models.TimeField()
    fee = models.CharField(max_length=4)
    date = models.DateField()
    description = models.TextField()
    contact = models.CharField(max_length=10)
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('showcase:event-index')


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()
    time = models.DateTimeField(timezone.now)
