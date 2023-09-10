from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_description = models.TextField(null = True, blank=True)
    is_completed = models.BooleanField(default=False)