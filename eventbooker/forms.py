from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('name', 'content',)
        widgets = {
            "name": forms.TextInput(attrs={'size': 10, 'title': 'Your name', 'required': True}),
            "content": forms.TextInput(attrs={'title': 'Your comment', 'required': True})
        }
