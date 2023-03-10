from django import forms
from django.forms import ClearableFileInput
from .models import Submit_article, Contact
from django.forms import Textarea, ClearableFileInput, TextInput, EmailInput


# It creates a form for the Contact model.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter your name',
                                     'style': 'width:600px'}),
            'email': EmailInput(attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter your email',
                                       'style': 'width:600px;'}),
            'message': Textarea(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter your message here...',
                       'style': 'width:600px;'})
        }


# A form class that is used to create a form for submitting an article.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Submit_article
        fields = ['title', 'author', 'university',
                  'email', 'abstract', 'keywords', 'doc_file']
        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter the title of the article',
                       'style': 'width:600px;'}),
            'author': TextInput(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter your full name',
                       'style': 'width:600px;'}),
            'university': TextInput(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter the name of your instituion',
                       'style': 'width:600px;'}),
            'email': EmailInput(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter your email address',
                       'style': 'width:600px;'}),
            'abstract': Textarea(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter abstract of the article',
                       'style': 'width:600px;'}),
            'keywords': TextInput(
                attrs={'class': 'form-control col-md-4 offset-md-4', 'placeholder': 'Enter the article keywords',
                       'style': 'width:600px;'}),
            'doc_file': ClearableFileInput(
                attrs={'class': 'form-control col-md-8 offset-md-5', 'style': 'width:300px;'}),
        }



