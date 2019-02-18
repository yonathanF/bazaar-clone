from django.test import TestCase

from .ApiWrapper import API


class ApiWrapperTestCase(TestCase):
    """
    Basic tests for the functionality of the wrapper
    """
    def setUp(self):
        self.api = API()

    def test_post_with_basic_args(self):
        url = '/profile/create/'
        response = self.api.post(url, {'first_name': 'yonathan',
                                       'last_name': 'fisseha',
                                       'education': 'uva',
                                       'description': 'stuff',
                                       'zip_code': 80012,
                                       'rating': 5})

        print(response)
