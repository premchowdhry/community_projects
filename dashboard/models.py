from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Dashboard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, default='')
    content = models.TextField(default='')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
