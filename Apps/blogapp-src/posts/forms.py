from django import forms

from .models import Post

class PostForm(forms.Form):
    title           = forms.CharField(max_length=240, required=False)
    descrption      = forms.CharField(max_length=240, required=False)
    image           = forms.ImageField()
    slug            = forms.CharField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image',
            'slug'
        ]