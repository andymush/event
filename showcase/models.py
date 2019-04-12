from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=40)
    venue = models.CharField(max_length=35)
    time = models.TimeField()
    fee = models.CharField(max_length=4)
    date = models.DateField()
    description = models.TextField()
    contact = models.CharField(max_length=10)
    cover = models.FileField()

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('showcase:event-index')


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('showcase:detail', args=[str(self.pk)])
