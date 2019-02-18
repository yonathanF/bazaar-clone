import datetime 
import json

from django.test import TestCase
from .models import Comment
from Post.models import Post
from UserProfile.models import Profile
from Post.PostChoiceConsts import Categories, Contact, Type
from .StarConstants import Stars
from .views import serialize_post

STATUS_OK = 200
STATUS_NOTFOUND = 404
STATUS_BAD = 400


# Create your tests here.


def create_test_comment():
	post1 = Post.objects.create(
			title = "Test Title",
			details = "This is a nice detail",
			category = Categories[1][0],
			preferred_contact = Contact[0][0],
			deadline = "2019-03-21",
			zip_code = 80012,
			request_type = Type[0][0]
		)

	user1 = Profile.objects.create(
			first_name = "Sally".
			last_name = "Sample",
			rating = 3,
			description = "This is a short bio", 
			education = "Bachelor's Degrees",
			zip_code = 22904
		)


    return Comment.objects.create(
            title = "Test Comment",
            details = "This is a comment about a particular post",
            stars = Stars[1][0],
            date_posted = "2019-03-21",
            post = post1,
            user = user1
        )





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










