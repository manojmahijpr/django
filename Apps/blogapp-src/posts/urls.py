from django.conf.urls import url

from .views import posts_list, posts_detail, posts_create

urlpatterns = [
    url(r'^$', posts_list),
    url(r'create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/', posts_detail),    
]
