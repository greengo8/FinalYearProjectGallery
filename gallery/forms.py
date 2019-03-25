from django import forms
from .models import GPost


class PostForm(forms.ModelForm):
    class Meta:
        model = GPost
        fields = ['title', 'cover']
