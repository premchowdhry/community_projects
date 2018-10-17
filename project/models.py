from django.db import models
from django.utils import timezone

class Project(Post):
    completed_content = models.TextField()
    date_completed = models.DateTimeField(default=timezone.now)
    number_likes = models.IntegerField()

    def __str__(self):
        return self.title
