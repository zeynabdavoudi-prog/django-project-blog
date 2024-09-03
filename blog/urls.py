from django.urls import path
from . import views
from .feeds import LatestEntriesFeed
app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('single/<int:post_id>', views.BlogSingleView.as_view(), name='blog_single'),
    path('category/<str:cat_name>', views.BlogView.as_view(), name='blog_category'),
    path('author/<str:author_username>', views.BlogView.as_view(), name='blog_author'),
    path('tag/<str:tag_name>', views.BlogView.as_view(), name='blog_tag'),
    path('search/', views.BlogSearchView.as_view(), name='blog_search'),
    path("rss/feed/", LatestEntriesFeed()),

]
