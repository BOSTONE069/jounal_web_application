from django.db import models

# Create your models here.

# It creates a class called ListItem that has two fields: item and order.
# The above class is a model for the Editorial Board of the journal. It has five fields: Prefix,
# FirstName, SecondName, University and Country
class Editorialboard(models.Model):
    Prefix = models.CharField(max_length=20, default="Prof")
    FirstName = models.CharField(max_length=100, default='Tom')
    SecondName = models.CharField(max_length=100, default= 'Kwanya')
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
