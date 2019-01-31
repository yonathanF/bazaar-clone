from django.db import models
from .OptionConstants import Categories

class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=900)
    date_posted = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    category = models.CharField(max_length=3, choices=Categories)
    zip_code = models.IntegerField()

     
