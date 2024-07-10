from django.urls import path
from django.views.generic import TemplateView

from a_posts import views

# Conf for sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'postpages': PostpageSitemap
}
urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
    path('', views.home_view, name='home'),
    path('post/create/', views.post_create, name='post-create'),
    path('category/<tag>/', views.home_view, name='category'),
    path('post/delete/<pk>/', views.post_delete, name='post-delete'),
    path('post/edit/<pk>/', views.post_edit, name='post-edit'),
    path('post/like/<pk>/', views.like_post, name='like-post'),
    path('comment/like/<pk>/', views.like_comment, name='like-comment'),
    path('reply/like/<pk>/', views.like_reply, name='like-reply'),
    path('post/<pk>/', views.post_detail, name='post-detail'),
    path('commentsent/<pk>/', views.comment_sent, name='comment-sent'),
    path('comment/delete/<pk>/', views.comment_delete, name='comment-delete'),
    path('replysent/<pk>/', views.reply_sent, name='reply-sent'),
    path('reply/delete/<pk>/', views.reply_delete, name='reply-delete'),

]
