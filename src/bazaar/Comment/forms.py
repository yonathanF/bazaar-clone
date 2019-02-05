from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Comment

class CreateCommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ['date_posted']
