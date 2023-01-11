from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, ArticleForm
from .models import Editorialboard, Editorinchief, Article
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
def index(request):
    """
    It takes a request, and returns a response

    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :return: The index.html file
    """
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
    articles = Article.objects.all().order_by('-volume')
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
            send_mail(
                'New Contact Form Submission',
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['bostoneochieng@gmail.com'],
                fail_silently=True,
            )
            messages.success(request, 'Message Sent Successfully')
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

def login_view(request):
    """
    If the request method is POST, then validate the form and log the user in

    :param request: The current request object
    :return: The login.html page is being returned.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('submit')
    else:
        form = AuthenticationForm()
    return render(request, 'rjikm/login.html', {'form': form})


def logout_view(request):
    """
    It logs the user out and redirects them to the logout_success view

    :param request: The current request object
    :return: The logout_view function is returning a redirect to the logout_success view.
    """
    logout(request)
    return redirect('login_view')


def register_view(request):
    """
    If the request method is POST, then we create a form object from the submitted data and save it to the database if it's
    valid. If the form is not valid, we re-render the template with the form object and any error messages. If the request
    method is not POST, then we create an empty form object and render it in the template

    :param request: The current request object
    :return: The render function is being returned.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('submit')
    else:
        form = UserCreationForm()
    return render(request, 'rjikm/register.html', {'form': form})


def view_pdf(request, id):
    """
    We open the PDF file, create an HttpResponse object with the PDF file as the content, set the
    Content-Disposition header to inline, and return the response

    :param request: The request object is used to get the current user
    :param id: The id of the article to be viewed
    :return: The PDF file is being returned as a response.
    """
    article = Article.objects.get(id=id)
    with open(article.pdf_doc.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=article.pdf'
        return response


def article_view(request, id):
    """
    The article_view function takes a request and an id, gets the article with the given id, and renders
    the article in the template.

    :param request: The request object is the first parameter to the view function. It contains
    information about the current request, such as the method (GET or POST), the user (if any is logged
    in), and the GET and POST parameters
    :param id: the id of the article
    :return: The article object
    """
    article = Article.objects.get(id=id)
    return render(request, 'rjikm/volarticles.html', {'article': article})
