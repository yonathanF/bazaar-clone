from django.db import models
from .StarConstants import Stars
#from .models import Post, UserProfile
from Post.models import Post
from UserProfile.models import Profile

# Create your models here.

class Comment(models.Model):
	title = models.CharField(max_length = 100)
	details = models.TextField()
	stars = models.CharField(max_length=3, choices=Stars)
	date_posted = models.DateTimeField(auto_now=True)
	#post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="creator")
	#user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="commenter")

	def publish(self):
		self.date_posted = timezone.now() 
		self.save()
