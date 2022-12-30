from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("editorial/", views.editorial, name="editorial"),
    path("articles", views. articles, name="articles"),
    path("contact", views.contact, name="contact"),
    path("submit/", views.submit, name="submit"),
    path("authorInstructions", views.authorInstructions, name="authorInstructions"),
    path("vol7articles/", views.vol7articles, name="vol7articles"),
    path("vol6_no2_articles", views.vol6_no2_articles, name="vol6_no2_articles"),
    path('rjikm/uploads/<int:pk>/download/', views.download_article, name='uploads'),
]
# default: "Django Administration"
admin.site.site_header = 'Regional Journal of Information and Knowledge Management'
# default: "Site administration"
admin.site.index_title = 'RJIKM'
# default: "Django site admin"
admin.site.site_title = 'HTML title from administration'
