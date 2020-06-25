from django import forms
from .models import Post, PostComment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')


class AddComment(forms.ModelForm):
    """Create comment form with html attributes set via widgets handlers
    for same."""
    class Meta:
        model = PostComment
        fields = [
            'comment'
        ]

    comment = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control',
            'placeholder': 'Add a comment'
        })
    )
