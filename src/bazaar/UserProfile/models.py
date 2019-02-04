from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(default='')
    education = models.CharField(max_length=200, default='')
    zip_code = models.IntegerField()
