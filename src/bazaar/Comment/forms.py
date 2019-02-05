from django import forms

class CommentForm(forms.Form):
	post = forms.CharField()