from django.test import TestCase
from .models import Comment
from Post.models import Post
from UserProfile.models import Profile
from .StarConstants import Stars
import datetime 


# Create your tests here.
class CreateCommentTestCase(TestCase):
	def setUp(self):
		Comment.objects.create(
			title="comment1", 
			details="this is good", 
			stars = Stars[0][0],
			date_posted = "1998-03-21",
			post_id = 1, 
			user_id = 1)
		Comment.objects.create(
			title="comment2",  
			details="this is bad", 
			stars = Stars[0][0],
			date_posted = "1998-03-21",
			post_id = 2, 
			user_id = 2)

	def test_comments_different_names(self):
		comment1 = Comment.objects.get(title="comment1")
		comment2 = Comment.objects.get(title="comment2")
		self.assertNotEqual(comment1, comment2)

	def test_comments_same_date(self):
		comment1 = Comment.objects.filter(date_posted= datetime.date[1998, 3, 21])
		print(comment1.count())
		comment2 = Comment.objects.filter(date_posted = datetime.date[1998, 3, 21])
		self.assertEqual(comment1, comment2)










