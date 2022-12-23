from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("editorial/", views.editorial, name="editorial"),
    path("articles", views.articles, name="articles"),
    path("contact", views.contact, name="contact"),
    path("submit/", views.submit, name="submit"),
    path('articles/<int:pk>/download/', views.download_article, name='download_article'),
]
# default: "Django Administration"
admin.site.site_header = 'Regional Journal of Information and Knowledge Management'
# default: "Site administration"
admin.site.index_title = 'RJIKM'
# default: "Django site admin"
admin.site.site_title = 'HTML title from administration'
