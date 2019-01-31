from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    rating = models.DecimalField(max_digits=1, decimal_places=2)
    description = models.TextField(default='')
    education = models.CharField(max_length=200, default='')
    zipcode = models.IntegerField(max_length=5)
