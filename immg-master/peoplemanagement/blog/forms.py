from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'content',
            'image'
        ]
