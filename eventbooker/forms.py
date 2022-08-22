from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('content',)
        widgets = {
            "content": forms.TextInput(attrs={'title': 'Your comment', 'required': True})
        }
# fix widget to display larger comment box - maybe integrate Crispy forms