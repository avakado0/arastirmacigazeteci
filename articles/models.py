from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField()
    content = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
