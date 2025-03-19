from taggit.forms import TagField
from django import forms
from .models import Post
from .models import Comment 
from taggit.forms import TagWidget 
# from .widgets import TagWidget  # Import from widgets.py if custom

from django.forms import widgets  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Apply TagWidget to the tags field
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body'] 