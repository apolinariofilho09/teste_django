from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    text_description=models.CharField(max_length=100)
    date_register=models.DateTimeField(auto_now_add=True)
    date_delivery=models.DateTimeField()
    date_complete=models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['date_delivery']

    def mark_as_completed(self):
        self.date_complete = datetime.now()
        self.save()

    def __str__(self):
        return self.text_description