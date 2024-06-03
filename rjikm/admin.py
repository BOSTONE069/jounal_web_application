from django.contrib import admin

from .models import *


# Register your models here.


# A class that inherits from the admin.ModelAdmin class.
class EditorialboardAdmin(admin.ModelAdmin):
    list_display = ['Prefix', 'FirstName', 'SecondName', 'University', 'Country']
    list_filter = ['FirstName', 'SecondName']
    search_fields = ('FirstName', 'SecondName')


# The class EditorinchiefAdmin is a subclass of the class ModelAdmin
class EditorinchiefAdmin(admin.ModelAdmin):
    list_display = ['FullName', 'Department', 'University', 'MyEmail']
    search_fields = ('FullName__startswith',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'department', 'email')
    search_fields = ('name', 'university', 'department')
    
# A class that inherits from the ModelAdmin class.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'volume', 'number', 'year', 'display_authors', 
                    'abstract_title', 'abstract', 'keyword_title', 'keywords', 'pdf_doc', 'is_archived')
    list_filter = ('is_archived', 'year', 'volume', 'number')
    search_fields = ('title', 'abstract', 'keywords', 'authors__name')
    filter_horizontal = ('authors',)


# A class that inherits from the ModelAdmin class. It is used to customize the admin interface.
class SubmittedAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'university', 'email', 'abstract', 'keywords', 'doc_file']


# It creates a list of the fields that will be displayed in the admin panel.
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


# Registering the Editorial board model with the Editorial boardAdmin class.
admin.site.register(Editorialboard, EditorialboardAdmin)
admin.site.register(Editorinchief, EditorinchiefAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Submit_article, SubmittedAdmin)
admin.site.register(Contact, ContactFormAdmin)
admin.site.register(Author, AuthorAdmin)
