from django.db import models
from django.utils import timezone


class Post(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=30)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    display_name = models.CharField(max_length=10, null=True, blank=True)
