from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('content',)
        content = forms.CharField(label="", help_text="", widget=forms.Textarea())

        
