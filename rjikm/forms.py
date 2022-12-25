import formatter
from django import forms
from django.forms import ClearableFileInput
from .models import Submit_article
from django.forms import Textarea, ClearableFileInput, TextInput, EmailInput


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Enter your message here...",
    }))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Submit_article
        fields = ['title', 'author', 'university',
                  'email', 'abstract', 'keywords', 'pdf_file']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder':'Enter the title of the article', 'style':'width:300px;'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name', 'style': 'width:300px;'}),
            'university': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of your instituion', 'style': 'width:300px;'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address', 'style': 'width:300px;'}),
            'abstract': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter abstract of the article', 'style': 'width:300px;'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the article keywords', 'style': 'width:300px;'}),
            'pdf_file': ClearableFileInput(attrs={'class': 'form-control-file', 'style': 'width:300px;'}),
        }
