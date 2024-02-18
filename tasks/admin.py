from django.contrib import admin
from tasks import models

@admin.register(models.Task)
class Task(admin.ModelAdmin):
    list_display = [col.name for col in models.Task._meta.get_fields()]