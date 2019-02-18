import datetime 
import json

from django.test import TestCase
from django.urls import reverse

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
			first_name = "Sally",
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


def comment_equals_form(comment, json_response):
    """
    Checks if the posts object is equal to the json object
    """

    if coment.title != json_response['title']:
        return False

    if coment.deadline != json_response['details']:
        return False

    if coment.details != json_response['stars']:
        return False

    if coment.category != json_response['date_posted']:
        return False

    if coment.preferred_contact != json_response['post']:
        return False

    if coment.zip_code != json_response['user']:
        return False

    return True



class CommentCreateTestCase(TestCase):
	def setUp(self):
		self.test_comment = create_test_comment()


	def test_wellFormatted_form_creates(self):

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
				first_name = "Sally",
				last_name = "Sample",
				rating = 3,
				description = "This is a short bio", 
				education = "Bachelor's Degrees",
				zip_code = 22904
			)

		response = self.client.post(
				reverse('createComment', kwargs={'post_id': post1.id, 'user_id': user1.id}),
				{
				'title' : "Test Comment",
				'details' : "This is a comment about a particular post",
				'stars' : Stars[1][0],
				'date_posted' : "2019-03-21",
				'post' : post1,
				'user' : user1
				})

		self.assertEqual(STATUS_OK, response.status_code)

		








