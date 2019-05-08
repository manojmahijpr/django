from django.conf.urls import url

from .views import BlogPostListView

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogPostListView.as_view(), name='blog-list')
]
