from django.db import models
from django.core.exceptions import ValidationError


class Conference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} {self.description}"

