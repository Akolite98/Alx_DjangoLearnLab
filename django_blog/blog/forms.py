from taggit.forms import TagField

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Allow users to add comma-separated tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
