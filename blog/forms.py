from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            max_length=50, 
            required=True
        )
    
    text = forms.CharField(
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            max_length=1000,
            required=True
        )

    class Meta:
        model=Post
        fields = ('title', 'text')
