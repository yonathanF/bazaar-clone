from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField

from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['date_posted']
