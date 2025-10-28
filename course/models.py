from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    trainers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'TRAINER'},
        related_name='trainer_courses'
    )
   

    def __str__(self):
        return self.title