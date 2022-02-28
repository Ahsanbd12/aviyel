from django.db import models
from aviyel_api.models import Conference, User
from django.core.validators import MinLengthValidator

class Talk(models.Model):
    title = models.CharField(validators=[MinLengthValidator(4)], max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    schedule_date = models.DateTimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
