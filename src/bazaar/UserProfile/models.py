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

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Profile, self).save(*args, **kwargs)

    def login(self, password):
        """
        Tries to login the user with the given password
        """
        return check_password(password, self.password)


class Authenticator(models.Model):
    user_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="tokens")
    authenticator = models.CharField(
        max_length=1024, default="defaultAuth", primary_key=True)
    date_created = models.DateTimeField(auto_now=True)
