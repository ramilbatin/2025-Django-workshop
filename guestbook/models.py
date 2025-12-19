from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Entry(models.Model):
    owner = models.ForeignKey(
                get_user_model(),
                on_delete=models.CASCADE,
                blank=True, null=True)
    
    message = models.TextField()
    datetime_created = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"