from django.db import models
from django.utils import timezone


class Name(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(
                                    max_length=30, null=True, blank=True
                                )
    last_name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
