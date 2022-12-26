from django.contrib import admin

from .models import Editorialboard, Editorinchief, Article, Submit_article, Contact


# Register your models here.


# A class that inherits from the admin.ModelAdmin class.
class EditorialboardAdmin(admin.ModelAdmin):
    list_display = ['Prefix', 'FirstName', 'SecondName', 'University', 'Country']
    list_filter = ['FirstName', 'SecondName']
    search_fields = ('FirstName', 'SecondName')


class EditorinchiefAdmin(admin.ModelAdmin):
    list_display = ['FullName', 'Department', 'University', 'MyEmail']
    search_fields = ('FullName__startswith',)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['volume', 'title', 'author1',  'department1', 'university1', 'email1', 'author2',  'department1', 'university2', 'email2', 'abstract_title', 'abstract', 'keyword_title',
                    'keywords', 'titlelink']
    list_filter = ["title"]
    search_fields = ('volume', 'title', 'author1',  'department1',
                     'university1', 'author2',  'department1', 'university2')


class SubmittedAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'university', 'email', 'abstract', 'keywords', 'pdf_file']


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


# Registering the Editorial board model with the Editorial boardAdmin class.
admin.site.register(Editorialboard, EditorialboardAdmin)
admin.site.register(Editorinchief, EditorinchiefAdmin)
admin.site.register(Article, ArticlesAdmin)
admin.site.register(Submit_article, SubmittedAdmin)
admin.site.register(Contact, ContactFormAdmin)
