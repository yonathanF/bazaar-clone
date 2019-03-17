import json
import unittest

from django.core import serializers
from django.test import Client, TestCase
from django.urls import reverse

from .models import Profile


class ProfilePasswordTestCase(TestCase):
    """
    Password related tests for the profile (user) model
    """

    def setUp(self):
        self.c = Client()


class getProfileTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='One',
            rating='2.22',
            description='model for unit test one',
            email="test@email.com",
            password="testPassword",
            education='test',
            zip_code='22903')

    @unittest.skip("Waiting on a fix for broken model")
    def test_getSuccess(self):
        response = self.c.get(
            reverse('change', kwargs={'profile_id': self.profile.id}))
        test = [
            'Test', 'One', '2.22', 22903, 'model for unit test one', 'test'
        ]
        response_list = []
        for k, v in response.json()['profile'].items():
            response_list.append(v)
        left = set(test)
        right = set(response_list)
        self.assertEquals(left, right)

    def test_getFailure(self):
        response = self.c.get(
            reverse('change', kwargs={'profile_id': 10000000000}))
        self.assertEquals(404, response.status_code)


class postProfileTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='Two',
            rating='4.44',
            email="test@email.com",
            password="testPassword",
            description='model for unit test two',
            education='test',
            zip_code='22903')

    @unittest.skip("Waiting on a fix for broken model")
    def test_postSuccess(self):
        response = self.c.post(
            reverse('create'), {
                'first_name': 'Test',
                'last_name': 'Two',
                'rating': '4.44',
                'email': 'testemail@email.com',
                'password': 'TestPassword',
                'description': 'model for unit test two',
                'education': 'test',
                'zip_code': '22903'
            })
        testid = self.profile.id
        profile = Profile.objects.filter(pk=testid)
        profile_json = json.loads(serializers.serialize('json', profile))
        self.assertEquals(profile_json[0]['fields'],
                          response.json()['profile'])

    def test_postFailure(self):
        response = self.c.post(
            reverse('create'), {
                'first_name': 'Test',
                'last_name': 'Two',
                'rating': '4.44',
                'email': 'testemail@email.com',
                'password': 'TestPassword',
                'description': 'model for unit test two',
                'education': 'test',
            })

        self.assertEquals(400, response.status_code)


class updateProfileTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='Three',
            rating='5.00',
            email="test@email.com",
            password="testPassword",
            description='model for unit test three',
            education='test',
            zip_code='22903')

    def test_updateSuccess(self):
        response = self.c.post(
            reverse('change', kwargs={'profile_id': self.profile.id}), {
                'first_name': 'Test',
                'last_name': 'Three',
                'rating': '1.00',
                'email': 'testemail@email.com',
                'password': 'TestPassword',
                'description': 'model for unit test three',
                'education': 'test',
                'zip_code': '22033'
            })

        response2 = self.c.get(
            reverse('change', kwargs={'profile_id': self.profile.id}))

        self.assertEquals(response.json(), response2.json())
        self.assertEquals(200, response.status_code)

    def test_updateFailure(self):
        response = self.c.post(
            reverse('change', kwargs={'profile_id': 1000000000}), {
                'first_name': 'Test',
                'last_name': 'Three',
                'email': 'testemail@email.com',
                'password': 'TestPassword',
                'rating': '1.00',
                'description': 'model for unit test three',
                'education': 'test',
                'zip_code': '22033'
            })

        self.assertEquals(404, response.status_code)


class deleteProfileTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='Three',
            rating='5.00',
            email="test@email.com",
            password="testPassword",
            description='model for unit test three',
            education='test',
            zip_code='22903')

    def test_deleteSuccess(self):
        response = self.c.get(
            reverse('delete', kwargs={'profile_id': self.profile.id}))

        self.assertEquals(200, response.status_code)
        response2 = self.c.get(
            reverse('delete', kwargs={'profile_id': self.profile.id}))
        self.assertEquals(404, response2.status_code)

    def test_deleteFailure(self):
        response = self.c.get(
            reverse('delete', kwargs={'profile_id': 10000000}))

        self.assertEquals(404, response.status_code)
