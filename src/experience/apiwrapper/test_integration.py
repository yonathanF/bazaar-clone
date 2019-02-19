from unittest.mock import MagicMock

from django.test import TestCase

from .ApiWrapper import API, APIV1

STATUS_OK = 200


class APIV1TestCase(TestCase):
    """
    Test cases for the v1 api wrapper
    """

    def setUp(self):
        self.server = API()

    def test_get_post(self):
        self.server.get = MagicMock(return_value={'test': 1})
        api = APIV1(self.server)

        self.assertEquals(api.post_get(1), {'test': 1})

    def test_post_post(self):
        self.server.post = MagicMock(return_value={'test': 1})
        api = APIV1(self.server)

        self.assertEquals(api.post_create(1), {'test': 1})


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

        status_code, response = self.api.get(get_url)

        self.assertEquals(STATUS_OK, status_code)

        self.assertEquals(response['profile']['first_name'],
                          post_data['first_name'])

        self.assertEquals(response['profile']['education'],
                          post_data['education'])

        self.assertEquals(response['profile']['zip_code'],
                          post_data['zip_code'])
