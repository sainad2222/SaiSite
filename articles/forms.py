from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']
        labels = {
            'title': 'title',
            'body': 'body',
            'slug': 'slug',
            'thumb': 'image',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control','placeholder': 'Enter title of the article'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control','placeholder': 'Article Body'          
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control','placeholder': 'Enter slug'          
            }),
            
        }