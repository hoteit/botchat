from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'issue_or_change', 'full_note', 'processed_note', 'date_field', 'cid')