from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


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
    It takes a request, and returns a response

    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: the render function.
    """
    return render(request, "rjikm/articles.html")

def editorial(request):
    """
    It takes a request, and returns a response

    :param request: The request object is an HttpRequest object. It contains metadata about the request,
    such as the HTTP method ("GET" or "POST"), the client's IP address, the query parameters, etc
    :return: the render function.
    """
    return render(request, "rjikm/editorialboard.html")

def submit(request):
    """
    It renders the submit.html template

    :param request: The request object is the first parameter to the view function. It contains
    information about the request that was made to the server
    :return: The submit.html page
    """
    return render(request, "rjikm/submit.html")

def contact(request):
    """
    If the form is valid, send the email and redirect to the success page

    :param request: The current HTTP Request object
    :return: The form is being returned.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email and redirect to success page
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, "rjikm/contact.html", {'form': form})