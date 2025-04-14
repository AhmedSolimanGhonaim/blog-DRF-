from django.db import models

# Create your models here.
from django.contrib.auth.models import User



# Our database model will have five fields: author, title, body, created_at, and updated_-
# at.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    