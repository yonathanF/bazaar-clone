import datetime 
import json

from django.test import Client, TestCase
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

def create_test_post():
	return Post.objects.create(
			title = "Test Title",
			details = "This is a nice detail",
			category = Categories[1][0],
			preferred_contact = Contact[0][0],
			deadline = "2019-03-21",
			zip_code = 80012,
			request_type = Type[0][0]
		)

def create_test_user():
	return Profile.objects.create(
				first_name = "Sally",
				last_name = "Sample",
				rating = 3,
				description = "This is a short bio", 
				education = "Bachelor's Degrees",
				zip_code = 22904
			)


def comment_equals_form(comment, json_response):
    """
    Checks if the posts object is equal to the json object
    """

    if comment.title != json_response['title']:
        return False

    if comment.details != json_response['details']:
        return False

    if comment.stars != json_response['stars']:
        return False

    if comment.date_posted != json_response['date_posted']:
        return False

    if comment.post != json_response['post']:
        return False

    if comment.user != json_response['user']:
        return False

    return True



class CommentCreateTestCase(TestCase):
	def setUp(self):
		self.test_comment = create_test_comment()


	def test_well_formatted_form_creates(self):

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
				reverse('createComment', kwargs={'post_id': self.test_comment.post.id, 'user_id': self.test_comment.user.id}),
				{
				'title' : "Test Comment",
				'details' : "This is a comment about a particular post",
				'stars' : Stars[1][0],
				'date_posted' : "2019-03-21",
				'post' : post1,
				'user' : user1
				})

		self.assertEqual(STATUS_OK, response.status_code)


	def test_malformed_form_doesnt_create(self):

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
				reverse('createComment', kwargs={'post_id': self.test_comment.post.id, 'user_id': self.test_comment.user.id}),
				{
				'title' : "Test Comment",
				'details' : "This is a comment about a particular post",
				'stars' : Stars[1][0],
				'date_posted' : "2019-xx-x1",
				'post' : 1,
				'user' : 2
				})

		self.assertEqual(STATUS_BAD, response.status_code)


class CommentDeleteTestCase(TestCase):
	"""
	Tests the delete endpoint for post
	"""
	def setUp(self):
		self.test_comment = create_test_comment()

	def test_exiting_comment_deleted(self):
		response = self.client.get(reverse('deleteComment', kwargs={'comment_id': self.test_comment.id}))

		self.assertEqual(STATUS_OK, response.status_code)

		json_response = json.loads(response.content.decode('utf-8'))
		self.assertIn(str(self.test_comment.id), json_response['Status'])

		response = self.client.get(
			reverse('viewComment', kwargs={'comment_id': self.test_comment.id}))

		self.assertEqual(STATUS_NOTFOUND, response.status_code)
		json_response = json.loads(response.content.decode('utf-8'))
		self.assertIn(str(self.test_comment.id), json_response['Status'])

	def test_nonexisting_post_not_deleted(self):
		non_existing_id = 499
		response = self.client.get(
			reverse('deleteComment', kwargs={'comment_id': non_existing_id}))

		self.assertEqual(STATUS_NOTFOUND, response.status_code)
		json_response = json.loads(response.content.decode('utf-8'))
		self.assertIn(str(non_existing_id), json_response['Status'])

class CommentGetTestCase(TestCase):
    """
    Tests the get endpoint for Post
    """
    def setUp(self):
        self.test_comment = create_test_comment()

    def test_existing_comment_returns(self):
        response = self.client.get(
            reverse('viewComment', kwargs={'comment_id': self.test_comment.id}))

        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertFalse(comment_equals_form(
                self.test_comment, json_response['comment']))


    def test_nonexisting_post_errors(self):
        non_existing_post = 498
        response = self.client.get(
            reverse('viewComment', kwargs={'comment_id': non_existing_post}))

        self.assertEqual(STATUS_NOTFOUND, response.status_code)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn(str(non_existing_post), json_response['Status'])


class CommentUpdateTestCase(TestCase):
    """
    Tests the update endpoint for Post
    """
	def setUp(self):
		self.test_comment = create_test_comment()
		self.test_post = create_test_post()
		self.test_user = create_test_user()

	def test_malformed_input_doesnt_update(self):
		updated_deadline = "2014x09x02"

        # a post to this endpoint is an update
		response = self.client.post(
			reverse('viewComment', kwargs={'comment_id': self.test_comment.id}),
				{
					'title': self.test_comment.title,
					'details': self.test_comment.details,
					'stars': self.test_comment.stars,
					'date_posted': updated_deadline,
					'post': test_post.id,
					'user': test_user.id
				})

		self.assertEqual(STATUS_BAD, response.status_code)


    def test_existing_comment_updates(self):
        updated_title = "Here's my new title"
        updated_details = "And also, here's a new detail!"

        # a post to this endpoint is an update
        response = self.client.post(
                reverse('viewComment', kwargs={'comment_id': self.test_comment.id}),
				{
					'title': self.test_comment.title,
					'details': self.test_comment.details,
					'stars': self.test_comment.stars,
					'date_posted': updated_deadline,
					'post': test_post.id,
					'user': test_user.id
				})

        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEquals(updated_zipcode,
                          json_response['comment']['title'])

        self.assertEquals(updated_deadline,
                          json_response['comment']['details'])

    def test_nonexisting_post_doesnt_update(self):
        updated_title = "Here's a third new title"
        updated_details = "here's a third revised description"

        # a post to this endpoint is an update
        response = self.client.post(
                reverse('viewPost', kwargs={'post_id': 400}),
                {
                    'title': self.test_post.title,
                    'details': self.test_post.details,
                    'category': self.test_post.category,
                    'preferred_contact': self.test_post.preferred_contact,
                    'deadline': updated_deadline,
                    'zip_code': updated_zipcode,
                    'request_type': self.test_post.request_type
                })

        self.assertEqual(STATUS_NOTFOUND, response.status_code)


class PostSerializationTestCase(TestCase):
    """
    Tests that posts are seralized as expected
    """
    def setUp(self):
        self.test_post = create_test_post()

    def test_nonexisting_post(self):
        response = serialize_post(400)
        self.assertEqual(STATUS_NOTFOUND, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn('400', json_response['Status'])

    def test_valid_post_serializes(self):
        response = serialize_post(self.test_post.pk)
        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))

        self.assertTrue(post_equals_form(
                self.test_post, json_response['post']))




























