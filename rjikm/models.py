from django.db import models


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
    
class Author(models.Model):
    name = models.CharField(max_length=100, default="Author Name")
    university = models.CharField(max_length=100, default="Name of the University")
    department = models.CharField(max_length=100, default="Name of the Department")
    email = models.EmailField(default="Enter your email address")
    
    def __st__(self):
        return f"{self.name}, {self.university}, {self.department}, {self.email}"


# It creates a model for the database.
class Article(models.Model):
    volume = models.IntegerField(default=1)
    number = models.IntegerField(default=1)
    year = models.IntegerField(default=2022)
    title = models.CharField(max_length=400, default='Untitled')
    authors = models.ManyToManyField(Author, related_name='articles')
    abstract_title = models.CharField(max_length=100, default='Abstract')
    abstract = models.TextField(default='No abstract provided')
    keyword_title = models.CharField(max_length=100, default="Keyword")
    keywords = models.CharField(max_length=200, default='None')
    pdf_doc = models.FileField(upload_to='rjikm/uploads/', default='Untitled')
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"Vol. {self.volume} No.{self.number} ({self.year}) - {self.title}"

    def delete(self, *args, **kwargs):
        # Delete the file associated with the object
        self.pdf_doc.delete()
        # Call the superclass's delete method
        super().delete(*args, **kwargs)

# It creates a model for the database.
class Submit_article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField()
    abstract = models.TextField()
    keywords = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='rjikm/uploads/')

    def delete(self, *args, **kwargs):
        # Delete the file associated with the object
        self.doc_file.delete()
        # Call the superclass's delete method
        super().delete(*args, **kwargs)


# It creates a model for the database.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
