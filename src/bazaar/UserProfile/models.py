import hmac
import os

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class Authenticator(models.Model):
    usr = models.ForeignKey(
        "UserProfile.Profile", on_delete=models.CASCADE, related_name="tokens")

    # TODO this is supposed to be unique but then it will be
    # have to be under 225 characters
    authenticator = models.CharField(max_length=1024)
    date_created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.authenticator = hmac.new(
            key=settings.SECRET_KEY.encode('utf-8'),
            msg=os.urandom(32),
            digestmod='sha256',
        ).hexdigest()

        super(Authenticator, self).save(*args, **kwargs)


class Profile(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField()
    password = models.CharField(max_length=1024, default="defaultPass")
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(default='')
    education = models.CharField(max_length=200, default='')
    zip_code = models.IntegerField()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Profile, self).save(*args, **kwargs)

    def login(self, password):
        if check_password(password, self.password):
            auth = Authenticator.objects.create(usr=self)
            return auth

        raise Exception("Incorrect password or email")

    def logout(self, auth_token):
        auths = Authenticator.objects.filter(usr=self)
        for auth in auths:
            if auth.authenticator == auth_token:
                auth.delete()
                return

        raise Exception("Not authorized for operation.")
