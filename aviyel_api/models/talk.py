from django.db import models
from django.core.exceptions import ValidationError
from aviyel_api.models import Conference, User

class Talk(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.TimeField()
    schedule_date = models.DateTimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
