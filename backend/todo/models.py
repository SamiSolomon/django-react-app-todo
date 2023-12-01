from django.db import models

# Create your models here.
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    # completed property is the status of the task, and we will set the default to False.
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
