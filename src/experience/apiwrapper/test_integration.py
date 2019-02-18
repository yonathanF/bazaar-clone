from django.test import TestCase

from .ApiWrapper import API

STATUS_OK = 200


class ApiWrapperTestCase(TestCase):
    """
    Basic tests for the functionality of the wrapper
    """
    def setUp(self):
        self.api = API()

    def test_post_with_basic_args(self):
        url = '/profile/create/'
        post_data = {'first_name': 'yonathan',
                     'last_name': 'fisseha',
                     'education': 'uva',
                     'description': 'stuff',
                     'zip_code': 80012,
                     'rating': 5}

        status_code, response = self.api.post(url, post_data)

        self.assertEquals(STATUS_OK, status_code)

        self.assertEquals(response['profile']['first_name'],
                          post_data['first_name'])

        self.assertEquals(response['profile']['education'],
                          post_data['education'])

        self.assertEquals(response['profile']['zip_code'],
                          post_data['zip_code'])

    def test_get_with_basic_args(self):
        url = '/profile/create/'
        post_data = {'first_name': 'yonathan',
                     'last_name': 'fisseha',
                     'education': 'uva',
                     'description': 'stuff',
                     'zip_code': 80012,
                     'rating': 5}

        status_code, response = self.api.post(url, post_data)
        self.assertEquals(STATUS_OK, status_code)

        get_url = '/profile/'+str(response['id'])
        get_data = {}

        status_code, response = self.api.get(get_url, get_data)

        self.assertEquals(STATUS_OK, status_code)

        self.assertEquals(response['profile']['first_name'],
                          post_data['first_name'])

        self.assertEquals(response['profile']['education'],
                          post_data['education'])

        self.assertEquals(response['profile']['zip_code'],
                          post_data['zip_code'])
