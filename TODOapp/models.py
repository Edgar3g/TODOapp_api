from django.db import models
import datetime
from django.utils import timezone


class Task(models.Model):
    TODO = 'ToDo'
    DONE = 'done' 

    TASK_STATUS = {
        (TODO, 'ToDo'),
        (DONE, 'Done')
    }

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=254)
    status = models.CharField(max_length=10, choices=TASK_STATUS, default=TODO)
    task_date = models.DateTimeField('data of task')

    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.task_date <= now