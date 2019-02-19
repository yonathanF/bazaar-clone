from django.db import models

from .PostChoiceConsts import Categories, Contact, Type


class Post(models.Model):
    """
    Represents a post requesting a services
    """

    title = models.CharField(max_length=100)
    details = models.CharField(max_length=900)
    category = models.CharField(max_length=3, choices=Categories)
    preferred_contact = models.CharField(max_length=2, choices=Contact)
    date_posted = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    zip_code = models.IntegerField()
    request_type = models.CharField(max_length=2, choices=Type)
    user = models.ForeignKey('UserProfile.Profile',
                             on_delete=models.CASCADE,
                             related_name="creator")
    comments = models.ForeignKey('Comment.Comment',
                             on_delete=models.CASCADE,
                             related_name="comment")
