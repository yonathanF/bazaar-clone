from django.db import models

from .StarConstants import Stars


class Comment(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    stars = models.CharField(max_length=3, choices=Stars)
    date_posted = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post.Post', on_delete=models.CASCADE, related_name="creator")
    user = models.ForeignKey('UserProfile.Profile', on_delete=models.CASCADE, related_name="commenter")
