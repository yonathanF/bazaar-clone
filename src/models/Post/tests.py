import json
from unittest import skip

from django.test import TestCase
from django.urls import reverse
from UserProfile.models import Profile

from .models import Post
from .PostChoiceConsts import Categories, Contact, Type
from .views import serialize_post

STATUS_OK = 200
STATUS_NOTFOUND = 404
STATUS_BAD = 400


def create_test_post():
    profile = Profile.objects.create(
        first_name="Yonathan",
        last_name="Fisseha",
        rating=4.0,
        description="Test description",
        education="University of Virginia",
        zip_code=80012)

    post = Post.objects.create(
        title="Test Title",
        details="This is a nice detail",
        category=Categories[1][0],
        preferred_contact=Contact[0][0],
        deadline="2019-03-21",
        zip_code=80012,
        request_type=Type[0][0],
        user=profile)
    return post, profile


def post_equals_form(post, json_response):
    """
    Checks if the posts object is equal to the json object
    """

    if post.title != json_response['title']:
        return False

    if post.deadline != json_response['deadline']:
        return False

    if post.details != json_response['details']:
        return False

    if post.category != json_response['category']:
        return False

    if post.preferred_contact != json_response['preferred_contact']:
        return False

    if post.zip_code != json_response['zip_code']:
        return False

    return True


class PostCreateTestCase(TestCase):
    """
    Tests the create endpoint for post
    """

    def setUp(self):
        self.test_post, self.test_profile = create_test_post()

    @skip("Broken. Waiting for a fix.")
    def test_wellFormatted_form_creates(self):
        response = self.client.post(
            reverse('createPost'), {
                'title': "New Title",
                'details': "Nice details",
                'category': Categories[1][0],
                'preferred_contact': Contact[0][0],
                'deadline': "1999-03-21",
                'zip_code': 82912,
                'request_type': Type[0][0],
                'user': self.test_profile.id
            })

        self.assertEqual(STATUS_OK, response.status_code)

    @skip("Broken. Waiting for a fix.")
    def test_malformed_form_doesnt_create(self):
        response = self.client.post(
            reverse('createPost'), {
                'title': "New Title",
                'details': "Nice details",
                'category': Categories[1][0],
                'preferred_contact': Contact[0][0],
                'deadline': "199-xx-21",
                'zip_code': 82912,
                'request_type': Type[0][0]
            })

        self.assertEqual(STATUS_BAD, response.status_code)


class PostDeleteTestCase(TestCase):
    """
    Tests the delete endpoint for post
    """

    def setUp(self):
        self.test_post, _ = create_test_post()

    def test_exiting_post_deleted(self):
        response = self.client.get(
            reverse('deletePost', kwargs={'post_id': self.test_post.id}))

        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn(str(self.test_post.id), json_response['Status'])

        response = self.client.get(
            reverse('viewPost', kwargs={'post_id': self.test_post.id}))

        self.assertEqual(STATUS_NOTFOUND, response.status_code)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn(str(self.test_post.id), json_response['Status'])

    def test_nonexisting_post_notdelted(self):
        non_existing_id = 499
        response = self.client.get(
            reverse('deletePost', kwargs={'post_id': non_existing_id}))

        self.assertEqual(STATUS_NOTFOUND, response.status_code)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn(str(non_existing_id), json_response['Status'])


class PostGetTestCase(TestCase):
    """
    Tests the get endpoint for Post
    """

    def setUp(self):
        self.test_post, _ = create_test_post()

    def test_existing_post_returns(self):
        response = self.client.get(
            reverse('viewPost', kwargs={'post_id': self.test_post.id}))

        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertTrue(
            post_equals_form(self.test_post, json_response['post']))

    def test_nonexisting_post_errors(self):
        non_existing_post = 498
        response = self.client.get(
            reverse('viewPost', kwargs={'post_id': non_existing_post}))

        self.assertEqual(STATUS_NOTFOUND, response.status_code)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn(str(non_existing_post), json_response['Status'])


class PostUpdateTestCase(TestCase):
    """
    Tests the update endpoint for Post
    """

    def setUp(self):
        self.test_post, self.test_profile = create_test_post()

    def test_malformed_input_doesnt_update(self):
        updated_deadline = "2014x09x02"

        # a post to this endpoint is an update
        response = self.client.post(
            reverse('viewPost', kwargs={'post_id': self.test_post.id}), {
                'title': self.test_post.title,
                'details': self.test_post.details,
                'category': self.test_post.category,
                'preferred_contact': self.test_post.preferred_contact,
                'deadline': updated_deadline,
                'zip_code': self.test_post.zip_code,
                'request_type': self.test_post.request_type,
                'user': self.test_profile.id
            })

        self.assertEqual(STATUS_BAD, response.status_code)

    def test_existing_post_updates(self):
        updated_zipcode = 90421
        updated_deadline = "2014-09-02"

        # a post to this endpoint is an update
        response = self.client.post(
            reverse('viewPost', kwargs={'post_id': self.test_post.id}), {
                'title': self.test_post.title,
                'details': self.test_post.details,
                'category': self.test_post.category,
                'preferred_contact': self.test_post.preferred_contact,
                'deadline': updated_deadline,
                'zip_code': updated_zipcode,
                'request_type': self.test_post.request_type,
                'user': self.test_profile.id
            })

        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEquals(updated_zipcode, json_response['post']['zip_code'])

        self.assertEquals(updated_deadline, json_response['post']['deadline'])

    def test_nonexisting_post_doesnt_update(self):
        updated_zipcode = 90421
        updated_deadline = "2014-09-02"

        # a post to this endpoint is an update
        response = self.client.post(
            reverse('viewPost', kwargs={'post_id': 400}), {
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
        self.test_post, _ = create_test_post()

    def test_nonexisting_post(self):
        response = serialize_post(400)
        self.assertEqual(STATUS_NOTFOUND, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))
        self.assertIn('400', json_response['Status'])

    def test_valid_post_serializes(self):
        response = serialize_post(self.test_post.pk)
        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))

        self.assertTrue(
            post_equals_form(self.test_post, json_response['post']))
