from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "rjikm/index.html")

def about(request):
    return render(request, "rjikm/about.html")

def contact(request):
    return render(request, "rjikm/contact.html")

def articles(request):
    return render(request, "rjikm/articles.html")

def editorials(request):
    return render(request, "rjikm/editorials.html")

def submit(request):
    return render(request, "rjikm/submit.html")
