from django.forms import ModelForm

from .models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
            model = Comment
            exclude = ['date_posted', 'user', 'post']
