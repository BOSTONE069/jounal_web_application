from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("editorial/", views.editorial, name="editorial"),
    # path('articles', views.articles, name='articles'),
    # path('article/<int:id>', views.article_view, name='article_view'),
    path("contact", views.contact, name="contact"),
    path("submit/", views.submit, name="submit"),
    path("authorInstructions", views.authorInstructions, name="authorInstructions"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('view_pdf/<int:id>', views.view_pdf, name='view_pdf'),
    path('rjikm/uploads/<int:pk>/download/', views.download_article, name='uploads'),
    path('current/', views.current_articles, name='current_articles'),
    path('archives/', views.archived_articles, name='archived_articles'),
    path('archive/<int:article_id>/', views.archive_article, name='archive_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# default: "Django Administration"
admin.site.site_header = 'Regional Journal of Information and Knowledge Management'
# default: "Site administration"
admin.site.index_title = 'RJIKM'
# default: "Django site admin"
admin.site.site_title = 'HTML title from administration'
