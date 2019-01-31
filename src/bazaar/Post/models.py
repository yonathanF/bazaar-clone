from django.db import models
from .OptionConstants import Categories

class Post(models.Model):
    title = models.CharField(max_field=100)
    details = models.CharField(max_field=900)
    date_posted = models.DateTimeField(auto_now=true)
    deadline = models.DateField()
    category = models.CharField(choices=Categories)
    location = models.IntegerField(max_length=5)
