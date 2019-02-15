import json

from django.test import Client, TestCase
from django.urls import reverse

from .models import Post
from .PostChoiceConsts import Categories, Contact, Type
from .views import serialize_post

STATUS_OK = 200


class PostSerializationTestCase(TestCase):
    """
    Tests that posts are seralized as expected
    """
    def setUp(self):
        self.test_post = Post.objects.create(
            title="Test Title",
            details="This is a nice detail",
            category=Categories[1][0],
            preferred_contact=Contact[0][0],
            deadline="2019-03-21",
            zip_code=80012,
            request_type=Type[0][0]
        )

    def test_valid_post_serializes(self):
        response = serialize_post(self.test_post.pk)
        self.assertEqual(STATUS_OK, response.status_code)

        json_response = json.loads(response.content.decode('utf-8'))

        self.assertEquals(self.test_post.title, json_response['post']['title'])
        self.assertEquals(self.test_post.deadline,
                          json_response['post']['deadline'])
        self.assertEquals(self.test_post.details,
                          json_response['post']['details'])
        self.assertEquals(self.test_post.category,
                          json_response['post']['category'])
        self.assertEquals(self.test_post.preferred_contact,
                          json_response['post']['preferred_contact'])
        self.assertEquals(self.test_post.zip_code,
                          json_response['post']['zip_code'])



