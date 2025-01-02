from django import forms
from .models import Cat, News
from django.forms import ModelForm, TextInput, Textarea


class AddPostForm(forms.ModelForm):
    

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'cat']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
        }