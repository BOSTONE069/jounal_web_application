from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, ArticleForm
from .models import Editorialboard, Editorinchief, Article
from django.contrib import messages
from django.core.mail import send_mail
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    return render(request, "rjikm/index.html")


def about(request):
    """
    It takes a request, and returns a response

    :param request: The request is an HttpRequest object
    :return: The about.html page is being returned.
    """
    return render(request, "rjikm/about.html")


def contact(request):
    """
    The function contact() takes a request object as an argument and returns a rendered template called
    contact.html

    :param request: The request is an HttpRequest object
    :return: The contact.html page is being returned.
    """
    return render(request, "rjikm/contact.html")


def articles(request):
    """
    It takes a request, gets all the articles from the database, and then renders the articles.html
    template, passing in the articles

    :param request: The request is an HttpRequest object. It contains metadata about the request, such
    as the client’s IP address, the HTTP method, and the headers
    :return: The articles.html template is being returned.
    """
    articles = Article.objects.all()
    return render(request, "rjikm/articles.html", {'articles': articles})


def editorial(request):
    """
    It takes a request, gets all the Editorialboard objects, and then renders the editorialboard.html
    template with the editorialboard objects

    :param request: The request is an HttpRequest object
    :return: The editorialboard variable is being returned.
    """
    editorialboard = Editorialboard.objects.all()
    editorinchief = Editorinchief.objects.all()
    return render(request, 'rjikm/editorialboard.html',
                  {'editorialboard': editorialboard, 'editorinchief': editorinchief})


def submit(request):
    """
    If the request is a POST request, then validate the form and save it. If the request is a GET
    request, then create a new form

    :param request: The request is a HttpRequest object. It contains metadata about the request, such as
    the HTTP method
    :return: The form is being returned.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article submitted successfully')
            return redirect('submit')
    else:
        form = ArticleForm()
    return render(request, "rjikm/submitmanuscritpt.html", {'form': form})


def contact(request):
    """
    If the request is a POST request, then validate the form and send an email to the admins.
    If the request is a GET request, then render the form.

    :param request: The request object is the first parameter to all Django views. It contains metadata
    about the request, such as the HTTP method ("GET" or "POST"), the client's IP address, the query
    parameters, and more
    :return: a render object.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send an email to the admins
            send_mail(
                'New Contact Form Submission',  # Subject
                form.cleaned_data['message'],  # Message
                form.cleaned_data['email'],  # From email
                ['bostoneochieng@gmail.com'],  # List of recipient emails
                fail_silently=True,
            )
            messages.success(request, 'Message Sent Successfully')
            # send email and redirect to success page
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "rjikm/contact.html", {'form': form})


def download_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    file = article.pdf_file
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response


def authorInstructions(request):
    """
    It takes a request, and returns a response

    :param request: The request object is a Python object that contains metadata about the request sent
    to the server
    :return: The authorInstructions function is returning the authorinstructions.html page.
    """
    return render(request, "rjikm/authorinstructions.html")


def vol7articles(request):
    """
    It's a function that takes a request and returns a render of the vol7articles.html template with the articles variable
    set to the articles variable

    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The articles are being returned.
    """
    articles = Article.objects.all()
    vol7_articles = []
    for article in articles:
        if vol7_articles == 'Vol. 7 No.1 (2022)':
            vol7_articles.append(article)
    return render(request, "rjikm/vol7articles.html", {'articles': articles})


def vol6_no2_articles(request):
    articles = Article.objects.all()
    vol6_no2_articles = []
    for article in articles:
        if vol6_no2_articles == "Vol. 6 No. 2 (2021)":
            vol6_no2_articles.append(article)
    context = {'articles': articles}
    return render(request, "rjikm/vol6articles.html", context)
