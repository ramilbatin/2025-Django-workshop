from django.contrib import admin
from . import models


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("id",)