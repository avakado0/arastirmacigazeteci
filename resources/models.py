from django.db import models

# Create your models here.

class Resource(models.Model):
    # Define your fields here
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
