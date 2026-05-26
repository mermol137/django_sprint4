"""Blog forms."""
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""

    class Meta:
        """Meta options for PostForm."""

        model = Post
        fields = [
            'title',
            'text',
            'location',
            'category',
            'pub_date',
            'image'
        ]
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments."""

    class Meta:
        """Meta options for CommentForm."""

        model = Comment
        fields = [
            'text'
        ]
