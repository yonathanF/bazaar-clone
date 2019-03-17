from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField()
    password = models.CharField(max_length=1024, default="defaultPass")
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(default='')
    education = models.CharField(max_length=200, default='')
    zip_code = models.IntegerField()

    def create_password(password):
        """
        Creates a hashed password of the plaintext passed in
        """
        pass

    def login(password):
        """
        Tries to login the user with the given password
        """
        pass
