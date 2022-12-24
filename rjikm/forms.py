from django import forms
from .models import Submit_article


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Enter your message here...",
    }))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Submit_article
        fields = ['title', 'author', 'university', 'email', 'abstract', 'keywords', 'pdf_file']
