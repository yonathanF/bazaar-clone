import json
import unittest

from django.core import serializers
from django.test import Client, TestCase
from django.urls import reverse

from .models import Authenticator, Profile


class ProfilePasswordTestCase(TestCase):
    """
    Password related tests for the profile (user) model
    """

    def setUp(self):
        self.c = Client()
        self.test_password = "testPassword",
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='One',
            rating='2.22',
            description='model for unit test one',
            email="test@email.com",
            password=self.test_password,
            education='test',
            zip_code='22903')

    def test_password_is_hashed(self):
        """
        Checks that the password passed in is hashed properly
        """
        self.assertNotEqual(self.test_password, self.profile.password)

    def test_correct_password_is_accepted(self):
        """
        Tests that correct passwords are accepted
        """
        profile = Profile.objects.get(pk=self.profile.pk)
        auth_profile = profile.login(self.test_password)
        auth_from_authenticator = Authenticator.objects.get(user=profile)
        self.assertEqual(auth_profile, auth_from_authenticator)

    def test_incorrect_password_is_rejected(self):
        """
        Tests that incorrect passwords are rejected
        """
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertRaises(Exception, profile.login, "WrongPassword")

    def test_auth_token_generated(self):
        """
        Tests that the authentication token is generated
        correctly for an existing user
        """
        auth = Authenticator.objects.create(user=self.profile)
        self.assertNotEqual(auth.authenticator, "")

    def test_logout_with_good_token(self):
        """
        Tests that logging out with a good token works
        """
        auth = self.profile.login(self.test_password)
        self.profile.logout(auth.authenticator)
        auths = Authenticator.objects.filter(user=self.profile)
        self.assertNotIn(auth, auths)

    def test_logout_with_bad_token(self):
        """
        Tests that logouts are rejected if the request
        doesn't have a good auth token
        """
        self.assertRaises(Exception, self.profile.logout, "badAuthToken")


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

    def test_getSuccess(self):
        response = self.c.get(
            reverse('change', kwargs={'profile_id': self.profile.id}))
        test = [
            'Test', 'One', '2.22', 22903, 'model for unit test one', 'test', "test@email.com"
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
        self.profile = {
            'first_name': 'Test',
            'last_name': 'Two',
            'rating': '4.44',
            'email': "test@email.com",
            'description': 'model for unit test two',
            'education': 'test',
            'zip_code': 22903
        }


    def test_postSuccess(self):
        response = self.c.post(
            reverse('create'), {
                'first_name': 'Test',
                'last_name': 'Two',
                'rating': '4.44',
                'email': 'test@email.com',
                'password': 'testPassword',
                'description': 'model for unit test two',
                'education': 'test',
                'zip_code': '22903'
            })

        self.assertEquals(self.profile,
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
