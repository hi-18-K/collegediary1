from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Project(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField(max_length = 500)
    date_posted = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    github_link = models.URLField(max_length=400)
    tag = models.TextField(max_length = 500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail',kwargs = {'pk': self.pk})
