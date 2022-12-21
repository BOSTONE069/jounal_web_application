from django.db import models

# Create your models here.

# It creates a class called ListItem that has two fields: item and order.
class ListItem(models.Model):
    item = models.CharField(max_length=200)
    order = models.PositiveIntegerField()