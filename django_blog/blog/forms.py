from taggit.forms import TagField
from django import forms
from .models import Post
from .models import Comment 
from django.forms import widgets  

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Allow users to add comma-separated tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body'] 