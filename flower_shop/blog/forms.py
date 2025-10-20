from django.forms import ModelForm
from .models import Comments
from django import forms


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

        labels = {
            'content': '',
        }

