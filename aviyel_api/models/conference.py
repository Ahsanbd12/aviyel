from django.db import models
from django.core.validators import MinLengthValidator

class Conference(models.Model):
    title = models.CharField(validators=[MinLengthValidator(4)],  max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} {self.description}"

