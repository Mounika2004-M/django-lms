from django.db import models
from django.conf import settings
from course.models import Course

# Create your models here.

class Batch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='batches')
    start_date = models.DateField()
    end_date = models.DateField()
    learners = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'LEARNER'},
        related_name='learner_batches'
    )
    trainners = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'TRAINER'},
        related_name='batches',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f" {self.name} {self.course.title} "