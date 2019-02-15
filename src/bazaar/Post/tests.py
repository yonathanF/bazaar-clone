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
        json_response = json.loads(response.json)

        self.assertEquals(self.test_post.title, json_response['post']['title'])
