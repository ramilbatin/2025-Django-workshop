from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "active", "date_posted",]
    list_filter = ["active", "date_posted",]