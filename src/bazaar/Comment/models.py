from django.db import models
from .StarConstants import Stars

# Create your models here.

class Comment(models.Model):
	title = models.CharField(max_length = 100)
	details = models.TextField()
	stars = models.CharField(max_length=3, choices=Stars)
	date_posted = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.date_posted = timezone.now() 
		self.save()
