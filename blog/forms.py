from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, PostComment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AddComment(forms.ModelForm):
    """Create comment form with html attributes set via widgets handlers
    for same."""
    class Meta:
        model = PostComment
        fields = [
            'comment_detail'
        ]

    comment_detail = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control border-black rounded-0',
            'placeholder': 'Comments...',
        })
    )

