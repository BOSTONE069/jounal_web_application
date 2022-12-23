from django.contrib import admin

from .models import Editorialboard, Editorinchief, Article, Submit_article


# Register your models here.


# A class that inherits from the admin.ModelAdmin class.
class EditorialboardAdmin(admin.ModelAdmin):
    list_display = ['Prefix', 'FirstName', 'SecondName', 'University', 'Country']


class EditorinchiefAdmin(admin.ModelAdmin):
    list_display = ['FullName', 'Department', 'University', 'MyEmail']


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['volume', 'title', 'author', 'university', 'email', 'abstract_title', 'abstract', 'keyword_title',
                    'keywords', 'titlelink']


class SubmittedAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'university', 'email', 'abstract', 'keywords', 'pdf_file']


# Registering the Editorialboard model with the EditorialboardAdmin class.
admin.site.register(Editorialboard, EditorialboardAdmin)
admin.site.register(Editorinchief, EditorinchiefAdmin)
admin.site.register(Article, ArticlesAdmin)
admin.site.register(Submit_article, SubmittedAdmin)
