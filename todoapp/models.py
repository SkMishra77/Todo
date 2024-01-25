# tasks/models.py
from django.db import models

from Todo.utils import Util
from accounts.models import User


class TaskModel(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'In Progress'),
        (2, 'Completed'),
    ]
    TaskId = models.CharField(primary_key=True, max_length=255, default=Util.generateTaskId)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'TaskModel'
        ordering = ('-created_at',)
