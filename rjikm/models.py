from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

# It creates a class called ListItem that has two fields: item and order.
# The above class is a model for the Editorial Board of the journal. It has five fields: Prefix,
# FirstName, SecondName, University and Country
class Editorialboard(models.Model):
    Prefix = models.CharField(max_length=20, default="Prof")
    FirstName = models.CharField(max_length=100, default='Tom')
    SecondName = models.CharField(max_length=100, default='Kwanya')
    University = models.CharField(max_length=100, default="Technical University of Kenya")
    Country = models.CharField(max_length=100, default="Kenya")

    def __str__(self):
        return f"{self.Prefix} {self.FirstName} {self.SecondName} {self.University} {self.Country}"


# The class Editorinchief is a model that has three fields: FullName, University and Email
class Editorinchief(models.Model):
    FullName = models.CharField(max_length=100, default='Tom')
    University = models.CharField(max_length=100, default="Technical University of Kenya")
    Department = models.CharField(max_length=100, default="Information and library Sciences")
    MyEmail = models.CharField(max_length=100, default="tom.kwanya@gmail.com")

    def __str__(self):
        return f" {self.FullName} {self.University} {self.MyEmail}"


# It creates a model for the database.
class Article(models.Model):
    volume = models.CharField(max_length=100, default="untitled")
    title = models.CharField(max_length=400, default='Untitled')
    author1 = models.CharField(max_length=100, default='Anonymous')
    university1 = models.CharField(max_length=100, default='Unknown')
    department1 = models.CharField(max_length=100, default='Unknown')
    email1 = models.EmailField(default='anonymous@example.com')
    author2 = models.CharField(max_length=100, default='Anonymous')
    department2 = models.CharField(max_length=100, default='Unknown')
    university2 = models.CharField(max_length=100, default='Unknown')
    email2 = models.EmailField(default='anonymous@example.com')
    abstract_title = models.CharField(max_length=100, default='Abstract')
    abstract = models.TextField(default='No abstract provided')
    keyword_title = models.CharField(max_length=100, default="Keyword")
    keywords = models.CharField(max_length=200, default='None')
    titlelink = models.CharField(max_length=400, default='Untitled')

    def __str__(self):
         return f"{self.volume} {self.title} {self.author1} {self.author2} {self.university1} {self.university2} {self.email1} {self.email2} {self.abstract_title} {self.abstract} {self.keyword_title} {self.keywords} {self.titlelink}"

# It creates a model for the database.
class Submit_article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField()
    abstract = models.TextField()
    keywords = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='rjikm/uploads/')


# It creates a model for the contact form.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
